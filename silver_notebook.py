# Databricks notebook source
dbutils.widgets.text("pipeline_name", "")
dbutils.widgets.text("pipeline_run_id", "")

pipeline_name = dbutils.widgets.get("pipeline_name")
pipeline_run_id = dbutils.widgets.get("pipeline_run_id")

# COMMAND ----------

print(f'Pipeline Name: {pipeline_name}')
print(f'Pipeline Run ID: {pipeline_run_id}')