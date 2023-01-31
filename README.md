# Python and Pandas Basic Text Analytics

Language Used: Python
Libraries Used: Regular Expressions, Pandas

Step 01: Parse text to CSV file
The sample text file is used to store initial unstructured data.

![image](https://user-images.githubusercontent.com/109261990/215699693-0c28871c-4069-4a19-b794-54741d7b0ac9.png)

 
The sample text file is imported to Python script and RegEx module is used to identify patterns to extract name, country and age. Then the data is further manipulated using Pandas library and exported to CSV format.

![image](https://user-images.githubusercontent.com/109261990/215699764-3abe3de6-922a-4ba5-b396-869c689e43ef.png)

Step 02: User modifies CSV file
Users can modify the CSV file after exporting. Eg: Add Occupation Column

![image](https://user-images.githubusercontent.com/109261990/215699809-c40bb0bf-7b34-47a4-a0d5-0041a50aa861.png)

 
Step 03: Convert the modified CSV to text file
The modified CSV file is then converted to standard format text file using Python Pandas library. The sentences are formatted to pre-defined structure.

![image](https://user-images.githubusercontent.com/109261990/215699833-ddfb3458-de98-446f-a3b7-f9d75dc822e8.png)

 
Step 04: Grouping
The modified CSV data is grouped using Python functions to identify the members who are over 30 years of age and members who are from Asian countries. Separate pre-defined array is used to store Asian countries list and they are matched with members’ country in modified CSV file. The output is stored in separate text files.

![image](https://user-images.githubusercontent.com/109261990/215699913-b70f665e-33ee-4403-8ac5-8c7f6d93533c.png)
 
 
Step 05: Identify members occupation exceptions
The sample text file contains some information about the occupations of specific members. (Eg: Alice is a student.) Those occupations are identified using pre-defined occupation list stored in a Python array. They are matched with the strings in the original sample file and stored in separate array for future reference.
The stored occupations are then checked with user modified occupation. If the user has modified with wrong occupation, the exceptions are captured while executing step 03. And the report is stored in separate text file.

![image](https://user-images.githubusercontent.com/109261990/215699956-5dde38f2-e10b-4aea-a9f6-bf2e3f877418.png)

 
