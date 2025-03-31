
# **Build a Delta Lakehouse Architecture on Databricks Using AWS Delta Lake**  
## **Game Sessions Activity Data Engineering Project**  

## **Project Overview**  

This project demonstrates a complete data engineering workflow, covering data generation, extraction, cleaning, transformation, and orchestration. The goal is to simulate game activity data (publishers, games, sessions, and activities) in JSON format, process it through various stages, and load it into a **Landing Zone** to feed the **Medallion Architecture** in Databricks.  

Once processed, the insights are visualized using **Databricks Dashboards** and **AI/BI Genie**, providing analytics on the global distribution and characteristics of game activities.  

Additionally, a **CI/CD workflow** is implemented to automatically deploy updates to the production environment whenever changes are made to the master branch.

---

## **Project Architecture**  
![Project Architecture](https://github.com/pmbemmo/Databricks_DEV/blob/main/gameactivity_lakehouse_project/requirements/Databricks_lakehouse-Architecture.png)

---

## **Technologies Used**  

This project utilizes the following technologies:  

- **SQL**: For the initialization of the lakehouse.
- **Python**: For data generation, extraction, and transformation.  
- **Faker Library**: For generating synthetic game activity data.  
- **AWS Delta Lake**: For scalable storage.  
- **Databricks**: For data warehousing, processing, and analytics.  
- **AI/BI Genie**: For building visualization dashboards.  
- **Databricks Workflows**: For job orchestration.  
- **GitHub**: For CI/CD and repository management.  

---

## **Data Generation**  

A Python script, using the **Faker** library, generates game activity data for **10 games** and their **10,000 player activities**. Two JSON files are created:  

### **1. Games.json**  
```json
{
  "publisher": "string",
  "game_info": {
    "game": {
      "GameID": "string",
      "Publisher": "string",
      "Rating": "string",
      "Genre": "string",
      "Game_Length": int,
      "Game_release_date": "date"
    }
  }
}
```

### **2. PlayerActivity.json**  
```json
{
  "player_activity": {
    "start_time": "DateTime",
    "end_time": "DateTime",
    "activity": {
      "PlayerID": "string",
      "GameID": "string",
      "SessionID": "string",
      "Activity_type": "string",
      "Level": int,
      "ExperiencePoints": float,
      "AchievementUnlocked": int,
      "CurrencyEarned": float,
      "CurrencySpent": float,
      "QuestCompleted": int,
      "EnemiesDefeated": int,
      "ItemsCollected": int,
      "Deaths": int,
      "DistanceTravelled": int,
      "ChatMessagesSent": int,
      "TeamEventsParticipated": int,
      "PlayMode": "string"
    }
  }
}
```

---

## **Data Processing Steps**  

### **1. Data Extraction**  

The generated JSON files are extracted from an **AWS S3 bucket**, organized in a **Landing Zone** directory:  

- **Games**: Contains game-related data.  
- **PlayerActivity**: Holds detailed session activity records.  

Key extracted attributes include:  

- Publisher  
- Genre  
- Rating  
- Activity Type  
- Dates (release, start, and end)  

---

### **2. Data Transformation**  

Once extracted, the raw data undergoes cleaning and transformation to improve quality and consistency.  
![Transformation](https://github.com/pmbemmo/Databricks-lakehouse/blob/0b92b0ad4a67bd441f19db6b86c9c5ac8e3fe14f/gameactivity_lakehouse_project/requirements/Data-transformation.png)

#### **Cleaning Processes**  

- Normalizing and translating text fields where necessary.  
- Adding metadata fields such as **insert** and **update timestamps**.  
- Handling missing values by replacing nulls with default values.  

---

### **3. Data Loading and Analytics**  

#### **AWS Delta Lake Storage**  
The transformed data is stored in **Databricks Volumes**, ensuring scalability for big data processing.  

#### **Databricks Warehouse**  
The structured data is moved from **Delta Lake** to **Databricks Warehouse**, enabling OLAP operations. SQL queries and aggregations are performed to derive key insights:  

- **Fact and dimension tables** (e.g., fact_player_activity,dim_game).
- **Aggregated session metrics** (e.g., average session duration). 
- **Aggregated genre metrics** (e.g., most popular game genres).  
- **Aggregated publisher metrics** (e.g., revenue by publisher).  

---

## **Visualization**  

The cleaned and structured data is visualized using **AI/BI Genie** with interactive dashboards:  

- **Distribution** of game genres.  
- **Top publishers** based on revenue and player engagement.  
- **Filters and drill-downs** for analyzing specific activity types.  

---

## **Orchestration**  

The entire workflow is **automated and scheduled** using **Databricks Workflows**.  

### **Key Components**  
- **Directed Acyclic Graphs (DAGs)**: Manage the sequence of tasks.  
- **Task Definitions**: Handle data extraction, transformation, and loading.  

This ensures an **efficient**, **scalable**, and **automated** data pipeline.  
![Worflow](https://github.com/pmbemmo/Databricks-lakehouse/blob/0b92b0ad4a67bd441f19db6b86c9c5ac8e3fe14f/gameactivity_lakehouse_project/requirements/Job-Workflow.png)


---

## **CI/CD Deployment**  

A **GitHub Actions-based CI/CD pipeline** automates deployment whenever changes are pushed to the **master branch**. This ensures:  

- **Version control** for data processing scripts.  
- **Automated testing and validation** before deployment.  
- **Seamless updates** to the production environment.  
![CICD](https://github.com/pmbemmo/Databricks-lakehouse/blob/fdf90ff8481a5202b9f0545ab18f2b10a4cbaf76/gameactivity_lakehouse_project/requirements/CICD-DeployToProd.png)

---


