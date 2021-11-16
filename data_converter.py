import pandas as pd
import sys
import csv
import json
import os.path


class DataConverter:
    def __init__(self):
        pass

    def isValidFile(self, filepath):
        """
        isValidFile
            - This method checks validity of the file and if file exists

        arguments:
            filepath: valid path to csv file

        returns:
            True: if file is valid

        raises:
            ValueError: if file is invalid or does not exist
        """
        try:
            if os.path.isfile(filepath) == False:
                return False

            with open(filepath, 'r') as csvfile:
                csv_dict = [row for row in csv.DictReader(csvfile)]
                if len(csv_dict) == 0:
                    return False

        except Exception as e:
            return False

        return True

    def convert_csv2json(self, **kwargs):
        """
        convert_csv2json
            - This method does conversion of client-specific csv data and converts them to json format

        arguments:
            kwargs['filepath']: valid path to csv file

        returns:
            converted_data: the json-formatted data
        """

        if kwargs['filepath'] is None:
            raise SyntaxError

        if self.isValidFile(kwargs['filepath']):

            converted_data = {
                                'label' : '',
                                'id' : '',
                                'link' : '',
                                'children' : {}
            }

            try:
                df = pd.read_csv(kwargs['filepath'])

                df = df.rename(columns=lambda x: x.replace(' ', ''))
                df = df.rename(columns=lambda x: x.upper())

                data_group = df.groupby(['LEVEL1-NAME',
                                        'LEVEL2-NAME',
                                        'LEVEL3-NAME'], as_index=False)

                for name,group in data_group:

                    #Convert df group to dictionary for easier referencing of values
                    group_dict = data_group.get_group(name).to_dict('list')

                    #Check if level2 exist from children of level1
                    level2_exist = True if name[1] in converted_data['children'] else False

                    #Set children of level2 if it exist, otherwise set to []
                    children = converted_data['children'][name[1]]['children'] if level2_exist else []

                    #Then build up level2 dictionary
                    level2 = {
                                'label' : name[1],
                                'id' : int(group_dict['LEVEL2-ID'][0]),
                                'link' : group_dict['LEVEL2URL'][0],
                                'children': children + [{
                                                            'label': name[2],
                                                            'id' : int(group_dict['LEVEL3-ID'][0]),
                                                            'link' : group_dict['LEVEL3URL'][0],
                                                            'children': []
                                                        }]
                    }

                    if level2_exist:
                        converted_data['children'][name[1]] = level2
                    else:
                        converted_data['children'] = {
                            **converted_data['children'], **{ name[1]: level2 }
                        }

                #Finally, merge everything to level1
                converted_data['label'] = group_dict['LEVEL1-NAME'][0]
                converted_data['id'] = int(group_dict['LEVEL1-ID'][0])
                converted_data['link'] = group_dict['LEVEL1-URL'][0]
                converted_data['children'] = list(converted_data['children'].values())

            except Exception as e:
                print (e)
                raise

            converted_data = json.dumps(converted_data)

            return converted_data


if __name__ == '__main__':

    try:
        print ('File: {}'.format(sys.argv[1]))
        file_path = sys.argv[1]

        print (DataConverter().convert_csv2json(filepath=file_path))

    except Exception as e:
        print ("Error: CSV file could not be found or invalid")
        usage = """
HOW TO RUN APPLICATION

OPTION 1: Run via Linux Terminal (for advanced users):
1. Open terminal and type:
        /usr/bin/python data_converter.py <path_to_csv_file>

        Ex:
        python data_converter.py 'data/data.csv'

OPTION 2: Run via Flask without Docker
1. Open terminal and type:
        python application.py
2. Open browser and access 'http://127.0.0.1:5000/'

OPTION 3: Run via Flask WITH Docker
1. Open terminal and type:
        'docker build –t <image_name> .'
        Example:
        docker build –t app_flask .
2. Verify if exists, type
        docker image ls
3. And then, run docker
        docker run  –p 5000:5000 <image_name>:advanced

OPTION 4: A sample Flask application is running, open any browser and type:
For sample running flask application, see:
        http://semilla-env.eba-n2kgtimw.us-east-1.elasticbeanstalk.com/

        """
        print (usage)