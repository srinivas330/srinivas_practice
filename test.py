import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
os.environ["PYSPARK_PYTHON"] = "C:/Users/Niwas/Documents/Python/Python/Python37/python.exe"  # or "python" depending on your Python executable
# Initialize a SparkSession
spark = SparkSession.builder.appName("KgToGramsConverter").getOrCreate()

# Sample data: weights in kilograms
data = [(1.0,), (2.5,), (0.75,), (10.0,)]
columns = ["weight_kg"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Convert kilograms to grams (1 kg = 1000 grams)
df_with_grams = df.withColumn("weight_g", col("weight_kg") * 1000)

# Show the DataFrame
df_with_grams.show()

# Stop the SparkSession