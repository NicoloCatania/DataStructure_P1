from pipeline import Pipeline

pipeline = Pipeline('C:\\Users\\Nico\\Documents\\GitHub\\DataStructure_P1\\pipeline')

# Creating a Show
pipeline.create_show(
    title='Demo Reel',
    description='A great show',
    release_date='2023-07-12',
    duration='60 minutes'
)

#Getting a List of Shows
shows = pipeline.get_all_shows()
for show in shows:
    print(show)


#Getting Information for a Show
show = pipeline.get_show('Demo Reel')
print(show)

#Updating Show Data
pipeline.update_show('Demo Reel', duration='45 minutes')

#Deleting a Show
pipeline.delete_show('Demo Reel')


#Creating a Shot within a Show
pipeline.create_shot(
    show_title='Demo Reel',
    shot_title='Opening Shot',
    description='The opening sequence',
    duration='5 minutes',
    status='In progress'
)

# Getting a List of Shots within a Show
shots = pipeline.get_all_shots('Demo Reel')
for shot in shots:
    print(shot)


# Getting Information for a Shot within a Show
shot = pipeline.get_shot('Demo Reel', 'Opening Shot')
print(shot)

# Updating Shot Data within a Show
pipeline.update_shot('Demo Reel', 'Opening Shot', status='Completed')

# Deleting a Shot within a Show
pipeline.delete_shot('Demo Reel', 'Opening Shot')
