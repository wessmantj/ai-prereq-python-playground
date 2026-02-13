import json 

if __name__ == '__main__': # makes it run when executed as a script and NOT when imported
    try: # for error handling, catches any execptions
        with open('input.json', 'r') as f: # opens file in read mode, r, using a context manager. The with statement automatically closes  after code block
            data = json.loads(f.read())  # reads entire file as a string using f.read() and parses into dictionary using json.loads()
        
        # ensure header generation is correct based on data structure
        if data:
            output = ','.join(data[0].keys())
        else:
            output = "" # handle empty list case

        for obj in data: 
            # convert all values to strings explicitly
            name = str(obj.get("Name", ""))
            age = str(obj.get("age", ""))
            birthyear = str(obj.get("birthyear", ""))
            output += f'\n{name},{age},{birthyear}' 
        
        with open('output.csv', 'w') as f: 
            f.write(output) 
    except Exception as ex:  # 
        print(f'Error: {str(ex)}')
