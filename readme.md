
# Local Data Lakehouse (MinIO + Spark + Jupyter + Trino)

This project sets up a local Data Lakehouse environment on my laptop using Docker.
It’s perfect for learning, data mining, analytics, and small-scale projects without relying on the cloud.

This project sets up a **local Data Lakehouse** environment using **Docker**, so you can practice and learn without any cloud dependencies.

We use the following tools:

* **MinIO** → S3-compatible storage (Data Lake layer)
* **Apache Spark** → Processing & ETL (Engine)
* **Jupyter Notebook (PySpark Notebook)** → Interactive analytics & coding
* **Trino (PrestoSQL)** → SQL engine for querying data in MinIO/Spark

---

##  Project Structure

```
lakehouse-project/
│
├── docker-compose.yml    # All services defined here
├── notebooks/            # Jupyter notebooks (code & experiments)
└── minio/                # Local data storage (MinIO backend)
    └── data/             # Files stored in MinIO (like S3 buckets)
```

---

## Setup Instructions

###  Clone/Create Project Folder

```bash
mkdir lakehouse-project
cd lakehouse-project
```

###  Create `docker-compose.yml`

Paste the following into a file named **docker-compose.yml**:

```yaml
services:
  minio:
    image: minio/minio
    container_name: minio
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ./minio/data:/data
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    command: server /data --console-address ":9001"

  spark:
    image: bitnami/spark:latest
    container_name: spark
    ports:
      - "7077:7077"
      - "8080:8080"

  spark-worker:
    image: bitnami/spark:latest
    container_name: spark-worker
    depends_on:
      - spark
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark:7077

  jupyter:
    image: jupyter/pyspark-notebook:latest
    container_name: jupyter
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work

  trino:
    image: trinodb/trino:latest
    container_name: trino
    ports:
      - "8081:8080"
```

---

###  Start the Environment

```bash
docker-compose up -d
```

Check running containers:

```bash
docker ps
```

---

##  How to Log In

### Jupyter Notebook

1. Open [http://localhost:8888](http://localhost:8888)
2. Copy the **token** from logs:

   ```bash
   docker logs jupyter
   ```

   Example:

   ```
   http://127.0.0.1:8888/lab?token=caf0fd65d279b07550d8d584092c0ada6bbda8a7a18c0bbe
   ```
3. Paste the token or just copy the full link into your browser. ✅

---

### MinIO (Object Storage)

1. Open [http://localhost:9001](http://localhost:9001)
2. Login credentials:

   * **Username**: `minioadmin`
   * **Password**: `minioadmin`

This is your **Data Lake layer** where raw data (CSV, JSON, Parquet) is stored.

---

### Spark Web UI

* Spark Master: [http://localhost:8080](http://localhost:8080)
* Workers will be visible here.

---

###  Trino Web UI

* Open [http://localhost:8081](http://localhost:8081)
* Run SQL queries on your data lake.

---

##  Data Lake Workflow

1. **Store Data** → Upload raw files (CSV/JSON/Parquet) to **MinIO**
2. **Process Data** → Use **Spark** (via Jupyter notebooks) for ETL/cleaning
3. **Query Data** → Use **Trino** to query processed data with SQL
4. **Analyze Data** → Build reports & ML models in **Jupyter**

---

##  Useful Commands

* Start environment:

  ```bash
  docker-compose up -d
  ```
* Stop environment:

  ```bash
  docker-compose down
  ```
* Restart a single service:

  ```bash
  docker restart jupyter
  ```
* Check logs:

  ```bash
  docker logs jupyter
  ```

---
