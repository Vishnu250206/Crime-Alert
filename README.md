# Crime-Alert:An Anonymous Crime Reporting System
## Description
The **Crime-Alert** System is an IT-enabled framework designed to empower individuals to report suspicious activities or crimes to the authorities efficiently and securely.Crime Alert serves as an anonymous crime reporting system, leverages blockchain technology for secure data storage and implements machine learning algorithms to detect potential false alarms. The system allows for anonymous reporting, ensuring user privacy, and includes features such as multimedia upload functionality, user feedback mechanisms, and support for user registration and authority login.

## Screenshots

Screenshots of the project's execution steps are as follows:

- Screenshot1:**HomePage**
  - This screenshot shows the homepage of the **CrimeAlert** application ![Screenshot1](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/Authority%20Homepage.jpg)
- Screenshot2: **SignUp Process**
  - In above screen click on ‘Signup Here’ link to get below page.In this screen user is entering sign up details and then press button to get Registered.
 ![Screenshot2](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/User%20SIgnup.jpg)
- Screenshot3:
  - In this screen,the red colour text can see sign up data saved in Blockchain  ![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/unique%20id.jpg)
- Screenshot4: **User HomePage**
  - In above screen user click on ‘User Login Here’ link to get below page and then user homepage will be displayed where you can submitTip,view the Submitted Tips,can submit Feedback Form![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/User%20LoginIn.jpg)
- Screenshot5: **Submitting a Tip**
  - In above screen user can click on ‘Submit Your Tip’ link to get below page and then the User input the suspicious activity details, upload images, and submit, saving information to the blockchain.![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/User%20Tipsubmission.jpg)
- Screenshot6: **Submitting Feedback**
  - In user HomePage,user can submit the Feedback Form.![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/User%20FeedbackForm.jpg)
- Screenshot7:
  - In this screen user can view all his submitted TIPS with images and in first column as username we have anonymised using AES algorithm to provide security to user details and in ‘Predicted Report Status’ can see CNN predicted as ‘True’ and now logout and login as Authority![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/User%20View%20Submitted%20Tips.jpg)
- Screenshot8: **Authority LoginIn**
  - In the HomePage of the Application,the authorities click on ‘Authority Login Here’ link to get below page and then the authority can login with their credentials
![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/Authority%20Login.jpg)
- Screenshot9: **AuthorityHomePage**
  - The authority HomePage screen will be displayed if the credentials are valid
 ![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/Authority%20Homepage.jpg)
- Screenshot10:
  - In above screen authority can click on ‘Train ML False Reporting Algorithm’ link to train algorithm on dataset and then will get prediction accuracy![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/False%20Reporting%20algorithm.jpg)
- Screenshot11: **Viewing Users Tips**
  - In this screen authority can see all tip details from all users in tabular format with ML predicted report status and username in anonymised format![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/View%20users%20Submitted%20Tips.jpg)



> [!NOTE]  
> The provided screenshots illustrate the execution flow of the application.

## Features

- **Anonymous Reporting :** Utilizes Blockchain technology to allow users to submit reports without requiring them to create an account or disclose personal information.
- **False Alarm Detection :** Implements machine learning algorithms to analyze submitted reports and identify potential false alarms, reducing unnecessary alerts for law enforcement.
- **Multi-media Upload Functionality :** Allows users to provide additional evidence or context when reporting incidents, enabling the upload of images related to the incidents.
- **User Feedback and Support :** Incorporates a feedback mechanism to gather user suggestions and improve the app continually. Provides a support system to address user queries or issues.
- **User Registration :** Generates random and unique IDs for user registration to ensure security and anonymity.
- **Authorities Login :** Implements a separate login system for authorities (e.g., law enforcement agencies) with appropriate credentials provided by the relevant organizations.


## Demo

Check out the [Crime Alert System Demo](https://drive.google.com/file/d/1EtTVwEbIR7MFhfHPJ8k2Hx7H4Z0fklOm/view?usp=drive_link) to see the system in action!


## Implementation Overview

- Utilizes Blockchain technology to securely store each record as a Block/transaction, ensuring data integrity.
- Employs a Smart Contract, designed using Solidity code, to save and retrieve data from the Blockchain.
- Each tip is displayed in a tabular format, with ML predictions from CNN aiding in decision-making.
- Data tampering prevention is ensured by verifying the hash code of all previous blocks before storing new records.

## Getting Started

>You can download the project files [here](https://github.com/20CSM-MAJOR-PROJECTS/PROJECT-BATCH-4/archive/refs/heads/master.zip)

### Deploying Smart Contract in Ethereum Tool

1.First go inside ‘hello-eth/node-modules/bin’ folder and then find and double click on ‘runBlockchain.bat’ file to start Ethereum tool and then will get below screen

2.In above screen Ethereum tool started with default private keys and account and now type command as ‘migrate’ and press enter key to deploy contract and then will get below page
![Screenshot3](https://github.com/Vishnu250206/Crime-Alert/blob/main/Screens/runtime%20pic.jpg)

3.In above screen in white colour text can see ‘Smart Contract’ deployed and got contract address also and this address need to specify in python code to save and get details from Ethereum and in below screen showing python code calling smart contract using address

To get started with the project, follow these steps:

1. **Start the IPFS Server:** Execute `runIPFS.bat` to start the IPFS server.
2. **Launch the Python Web Server:** Run `runServer.bat` to launch the Python web server.
3. **Access the Application:** Open a web browser and navigate to [http://127.0.0.1:8000/index.html](http://127.0.0.1:8000/index.html).
4. **Follow On-Screen Instructions:** Follow the on-screen instructions to sign up, submit tips, and utilize other functionalities.
## Team Members

- N.Nagasivani
- A.Srija Reddy
- M.Naga Sundeep
- G.Vishnu Chaitanya
## License

[MIT]@20CSM_B04

