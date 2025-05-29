# 📈 Monitoring Deployed Machine Learning Models with Prometheus and Grafana via MLflow

## 🔍 Overview

This project showcases how to monitor deployed Machine Learning models in real-time using **MLflow**, **Prometheus**, and **Grafana**. It involves deploying a machine learning model via MLflow's REST API, tracking key metrics (latency, accuracy, request count), and visualizing these metrics with Grafana for better observability in production environments.

---
## Authors

| Name                     | Student ID |
| ------------------------ | ---------- |
| **Quy Nhan Le**   | 22520999   |
| **Minh Quan Bui**       | 22521173   |
| **Tien Dat Nguyen Pham** | 22520217   |

## ⚙️ Architecture

```text
             ┌──────────────┐
             │ ML Model     │
             │ (via MLflow) │
             └─────┬────────┘
                   │
       Inference API (REST)
                   │
             ┌─────▼───────────┐
             │ Custom Exporter │ ◄── exposes metrics (latency, count)
             └─────┬───────────┘
                   │
          ┌────────▼────────┐
          │  Prometheus     │ ◄── scrapes metrics
          └────────┬────────┘
                   │
            ┌──────▼───────┐
            │   Grafana    │ ◄── visualizes metrics
            └──────────────┘
```

## 🧰 Technologies Used
MLflow – Model deployment and tracking

Python – Custom Prometheus exporter

Prometheus – Metrics collection

Grafana – Real-time dashboard & alerts

prometheus_client – Python library to expose metrics

## 🚀 Features
✅ Deploy ML model via MLflow REST API

✅ Expose custom inference metrics (latency, count, accuracy)

✅ Real-time monitoring with Prometheus

✅ Dynamic dashboards and alerts using Grafana

## 📷 Demo Screenshots
![demo1](https://github.com/user-attachments/assets/ec554a48-e3a7-4e6b-9e26-296d303e7e69)

![demo2](https://github.com/user-attachments/assets/1322cf19-6914-4b41-8688-83c5e35ef641)

![demo3](https://github.com/user-attachments/assets/32156545-0cee-4503-a6c7-fa1d644e355b)

![demo4](https://github.com/user-attachments/assets/75344ef3-97e3-4fc0-b978-e6cc543499ed)

## Sequence Diagram

sequenceDiagram
    participant User
    participant Terraform
    participant AWS
    participant MLflow
    participant Prometheus
    participant Grafana
    participant MLflow_Exporter

    User->>Terraform: Apply Terraform Config (AWS Infra/)
    Terraform->>AWS: Provision Infrastructure (EC2, VPC, SGs)
    AWS-->>Terraform: Infrastructure Ready
    User->>MLflow: Run main.py (Model Training)
    MLflow->>MLflow: Train Models, Log Metrics/Artifacts
    MLflow->>MLflow: Register Model
    MLflow->>MLflow_Exporter: Expose MLflow Metrics
    MLflow_Exporter->>Prometheus: Expose Metrics (Port 8000)
    Prometheus->>Prometheus: Scrape Metrics from MLflow_Exporter
    Prometheus->>Grafana: Data Source
    Grafana->>Grafana: Visualize Metrics (Dashboard)
    User->>Grafana: Access Grafana Dashboard (Port 3000)

