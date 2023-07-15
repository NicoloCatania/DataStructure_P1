Data Model
The data model of my pipeline code consists of two main classes: Show and Shot. These classes represent shows and shots in a pipeline and provide methods to convert the data to dictionaries and vice versa. The Pipeline class manages the pipeline of shows and shots.

Show
The Show class represents a show in the pipeline. It has the following properties:

title (string): The title of the show.
description (string): A description of the show.
release_date (string): The release date of the show.
duration (string): The duration of the show.
shots (list of Shot objects): A list of shots within the show.

Rationale
title, description, release_date, and duration are represented as strings because they are textual information.
shots is represented as a list of Shot objects to maintain the relationship between shows and shots. It allows easy access to the shots belonging to a show and enables organizing shots within a show.

Shot
The Shot class represents a shot within a show. It has the following properties:

title (string): The title of the shot.
description (string): A description of the shot.
duration (string): The duration of the shot.
status (string): The status of the shot (e.g., "Pending," "In Progress," "Completed").
Rationale
title, description, duration, and status are represented as strings because they are textual information.
status is represented as a string to allow flexibility in defining different status values. It can be easily customized to match specific workflow requirements (e.g., using predefined status codes).

FileHandler
The FileHandler class provides utility methods for handling file operations, such as creating directories, reading JSON files, writing JSON files, and deleting directories.

Rationale
The FileHandler class encapsulates common file operations to ensure clean and reusable code. It separates the file-related functionalities from the main logic of the Pipeline class, promoting modular and maintainable code.

Pipeline
The Pipeline class manages the pipeline of shows and shots. It has the following properties and methods:

base_dir (string): The base directory path where the pipeline data is stored.
file_handler (FileHandler object): An instance of the FileHandler class for handling file operations.
Rationale base_dir is represented as a string to store the base directory path. It allows customization of the storage location based on the specific needs of the application or system.
file_handler is an instance of the FileHandler class to separate file-related operations from the core functionality of the Pipeline class. It promotes better code organization and maintainability.

Data Serialization
To store and retrieve data, the to_dict() and from_dict() methods are provided in both the Show and Shot classes. These methods convert the object data to a dictionary representation and vice versa, allowing easy serialization and deserialization of the data.

Rationale
The data serialization methods facilitate storing and retrieving data in a structured format (JSON) while preserving the class structure and relationships. It enables data persistence and seamless integration with external systems or storage solutions.

