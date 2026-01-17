import json 

if __name__ == '__main__': 
    try: 
        with open('input.json', 'r') as f: 
            data = json.loads(f.read()) 
        
        # Ensure header generation is correct based on data structure
        if data:
            output = ','.join(data[0].keys())
        else:
            output = "" # Handle empty list case

        for obj in data: 
            # Convert all values to strings explicitly
            name = str(obj.get("Name", ""))
            age = str(obj.get("age", ""))
            birthyear = str(obj.get("birthyear", ""))
            output += f'\n{name},{age},{birthyear}' 
        
        with open('output.csv', 'w') as f: 
            f.write(output) 
    except Exception as ex: 
        print(f'Error: {str(ex)}')
