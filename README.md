# DataStructure_P1
The Pipeline Data Structure is a Python library that provides a simple way to manage shows and shots within a production pipeline. It allows you to create, retrieve, update, and delete shows and shots, along with their associated metadata.

# Installation
To use the Pipeline Data Structure library, you need to have Python installed on your system. You can then install the library using pip:

pip install pipeline



# Usage
To get started with the Pipeline Data Structure, you need to import the Pipeline class from the pipeline module:

from DataStructuresAPI import Pipeline



# Creating a Pipeline Instance
To create an instance of the pipeline, you need to provide the base directory where the show and shot data will be stored:

pipeline = Pipeline('/path/to/base_directory')
pipeline = Pipeline('C:\\Users\\Nico\\Documents\\GitHub\\DataStructure_P1\\pipeline')



# Creating a Show
To create a show, you can use the create_show method, specifying the title, description, release date, and duration:

pipeline.create_show(
    title='Demo Reel',
    description='My Reel',
    release_date='2023-08-01',
    duration='1 minute'
)



# Getting a List of Shows
To retrieve a list of all shows, you can use the get_all_shows method:

shows = pipeline.get_all_shows()
for show in shows:
    print(show.title)



# Getting Information for a Show
To retrieve information about a specific show, you can use the get_show method, providing the show title:

show = pipeline.get_show('Demo Reel')
print(show.title)
print(show.description)
print(show.release_date)
print(show.duration)



# Updating Show Data
To update the data of a show, you can use the update_show method, specifying the show title and the attributes you want to update:

pipeline.update_show('Demo Reel', description='My Reel')



# Deleting a Show
To delete a show and all its associated shots, you can use the delete_show method, providing the show title:

pipeline.delete_show('Demo Reel')



# Creating a Shot within a Show
To create a shot within a show, you can use the create_shot method, specifying the show title, shot title, description, duration, and status:

pipeline.create_shot(
    show_title='Demo Reel',
    shot_title='Shot1010',
    description='A great shot',
    duration='120 frames',
    status='In progress'
)



# Retrieving Shots within a Show
To retrieve a list of all shots within a show, you can use the get_all_shots method, providing the show title:

shots = pipeline.get_all_shots('Demo Reel')
for shot in shots:
    print(shot.title)



# Retrieving Shot Information within a Show
To retrieve information about a specific shot within a show, you can use the get_shot method, providing the show title and shot title:

shot = pipeline.get_shot('Demo Reel', 'Shot1010')
print(shot.title)
print(shot.description)
print(shot.duration)
print(shot.status)



# Updating Shot Data within a Show
To update the data of a shot within a show, you can use the update_shot method, specifying the show title, shot title, and the attributes you want to update:

pipeline.update_shot('Demo Reel', 'Shot1010', status='Completed')



# Deleting a Shot within a Show
To delete a shot within a show, you can use the delete_shot method, providing the show title and shot title:

pipeline.delete_shot('Demo Reel', 'Shot1010')

# DataStructure_P1
