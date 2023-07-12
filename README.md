# Study Portal Readme

This Study Portal is a web application built with Django, designed to help students manage their study tasks effectively. It provides features such as a todo list, homework management, YouTube integration, note-taking, conversion tools, and access to Wikipedia.

## Getting Started

To run the Study Portal locally, follow these steps:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/your-username/study-portal.git
   ```
2. Navigate to the project directory:
   ```
   cd study-portal
   ```
3. Create and activate a virtual environment (optional, but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set up the database:
   ```
   python manage.py migrate
   ```
6. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set a username and password.
7. Start the development server:
   ```
   python manage.py runserver
   ```
8. Access the Study Portal in your web browser at `http://localhost:8000`.

## Features

### Todo List
- Students can create a todo list to keep track of tasks they need to complete.
- They can add, edit, and delete tasks.
- Completed tasks can be marked as done.

### Homework Management
- Students can manage their homework assignments.
- They can add new assignments with due dates and descriptions.
- Homework can be marked as completed.

### YouTube Integration
- The Study Portal integrates with YouTube to help students access educational videos.
- Students can search for videos, watch them directly on the website, and add them to their favorites for later reference.

### Note-Taking
- The portal provides a note-taking feature to help students jot down important information.
- They can create and organize notes by topics or subjects.
- Notes can be edited and deleted as needed.

### Conversion Tools
- Students have access to conversion tools for common units of measurement.
- They can convert values between different units, such as length, weight, temperature, and more.
- This feature helps students easily convert values for assignments or experiments.

### Wikipedia Access
- The Study Portal offers access to Wikipedia for quick reference and research.
- Students can search for articles on various topics and read the content directly within the portal.

## Contributing

Contributions to the Study Portal are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your changes.
3. Make your desired changes and additions.
4. Test your changes to ensure they work as expected.
5. Commit your changes with descriptive commit messages.
6. Push your branch to your forked repository.
7. Submit a pull request to the original repository, explaining your changes and why they should be merged.

## License

The Study Portal is open source and released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

The Study Portal was developed by [Your Name] as a personal project. It was built using the Django web framework and incorporates various libraries and APIs to provide its functionality. Special thanks to the Django community, YouTube API, Wikipedia, and the developers behind the conversion libraries used in this project.
