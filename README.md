# Generate Groups

Randomly distribute members by groups making sure that every sector is represented

# The Scenario 

Imagine that you have a large group of people, coming from different areas. You need to create small groups where every area is represented. 

This small script allows you to do that. 

# CSV Structure example 

This is **sample data** randomly generated

|name|sector|department|
|:---|:---|:---|
Ingrid Carter	|	IT	|	radar 
Catherine Moody	|	IT	|	fin
Dax Rangel	|	IT	|	roof
Simeon Fuentes	|	MKT	|	shelf
Ismael Mccoy	|	MKT	|	radar 
Christine Kaiser	|	MKT	|	fin
Genevieve Reilly	|	PROD	|	roof
Bria Gomez	|	PROD	|	shelf
Giselle Frye	|	PROD	|	radar 
Simeon Ware	|	HR	|	fin
Jane Rubio	|	HR	|	roof
Taylor Tyler	|	HR	|	shelf

# Resulting CSV file 

This is **sample data** randomly generated

|  |name |	sector |department |	group|
|:---|:---|:---|:---|:---|
11	|	Taylor Tyler	|	HR	|	shelf	|	1
0	|	Ingrid Carter	|	IT	|	radar	|	1
4	|	Ismael Mccoy	|	MKT	|	radar	|	1
6	|	Genevieve Reilly	|	PROD	|	roof	|	1
10	|	Jane Rubio	|	HR	|	roof	|	2
1	|	Catherine Moody	|	IT	|	fin	|	2
3	|	Simeon Fuentes	|	MKT	|	shelf	|	2
8	|	Giselle Frye	|	PROD	|	radar	|	2
9	|	Simeon Ware	|	HR	|	fin	|	3
2	|	Dax Rangel	|	IT	|	roof	|	3
5	|	Christine Kaiser	|	MKT	|	fin	|	3
7	|	Bria Gomez	|	PROD	|	shelf	|	3

# How to run 

See requirements.txt file 

Run app.py from your terminal 






