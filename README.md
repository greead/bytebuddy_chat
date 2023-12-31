## ACS-560 Software Engineering

## Members:
- James Elliott
- Alekzander Green
- Aakansha Arora
- Khoa Nguyen

### Project Name

- ByteBuddy: the Coding Chatroom

### What will the project do?
ByteBuddy is a versatile programming assistance application designed to empower students in
their coding endeavors. The application enables students to create chat rooms where they can
seek assistance, collaborate, and receive guidance on their programming and coding projects.
What sets ByteBuddy apart is its integrated code editing and execution capabilities, allowing
students to write, edit, and run code seamlessly within the application.

### Who will benefit from this project?
- Enhanced Learning: Students can learn and practice coding collaboratively, improving their problem-solving skills and code quality through peer review
- Remote Learning: The platform facilitates remote collaboration and learning, making it suitable for distance education
- Instructor Feedback: Instructors can monitor student progress, offer guidance, and provide timely feedback
- Coding Portfolio: Users can build a portfolio of coding projects, which can be valuable for showcasing their skills to potential employers
- Community Building: The platform fosters a sense of community among computer science students, encouraging knowledge sharing and collaboration

### What data will be saved in database?
- Users: name, email, password (encrypted), owned chatrooms, state, and profile picture
- Chatrooms: name, tagline, creator, time created, last message time, active users, and whitelisted users
- Messages: content (text, emojis, images), time sent, sender, and chatroom
- Embedded IDE Information: contents, chatroom
- Direct Messages (maybe): same as messages + receiver

### What will be the easiest part of this project?
- Chat message sycronization
- Sending notifications for messages updates
- Interacting with other students within the application

### What will be the most difficult part of this project?
- Embedding the code editor
- Running the user code and/or returning results
- Allowing everyone in the chat room to see changes in editor in realtime
- Using eventing to update the frontend when changes occur in the backend