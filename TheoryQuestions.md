**Theory Questions and Answers**
by Tina Pinialidi

**1.1 What does SDLC stand for?**

SDLC stands for Software Development Lifecycle.

**1.2 What exception is thrown when you divide a number by 0?**

The exception thrown is the 'ZeroDivisionError' because it is not possible to divide a number by zero.

**1.3 What is the git command that moves code from the local repository to the remote repository?**

The command is git push.

**1.4 What does NULL represent in a database?**

NULL represents a null value which means that there is no value (data does not exist for the specific record).

**1.5 Name 2 responsibilities of the Scrum Master**

One responsibility of the Scrum Master is to coach team members on Scrum principles and best practice, and to help them understand what is expected of them and what the scope of the project is.

Another responsibility of the Scrum Master is to identify and remove issues and obstacles that affect the team and hinder the progress of the project.

**1.6 Name 2 debugging methods, and when you would use them.**

Method 1: Print statements. We can use print statements in any part of our code to view what the output of code is. This can help identify issues and change our code accordingly if the outcome is not correct. It is a simple and quick method so it is more suitable for easy to fix bugs that we can track along the way.

Method 2: We can utilise the built-in python debugger (pdb) using breakpoints to stop code at specific points and monitor what it does (step by step). This method can be used for more complex and harder to identify issues like iterations (for loops, while loops, etc.).

**1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need.**

The function would throw an error if one of the arguments is a string and the other is an integer or float. This would be a type error because we cannot compare an integer or float to a string. We can use try and except to catch a type error (and customise the error message if we want to) so that the program does not break when the exception occurs.

**1.8 What is git branching? Explain how it is used in Git.**

In Git, the main branch is the default branch which has the latest version of code for our project. However, if we want to make some modification or alter a feature, it is best to not work directly on the main branch and risk altering something on the project while we are still experimenting with those
modifications. For this reason, we can use branches; with the command ‘git branch’ we can create a new branch which is essentially a parallel version of the latest version of the project we have in main branch. While on that branch, we can experiment on that ‘parallel’ version and make any alterations, test code and see the results without affecting our main branch. When we are confident that the change can be implemented on our main branch, we can push the changes from the branch, and then create a pull request to review and merge those changes to the main branch. When merged, the latest version of our project on the main branch will include the changes from the other branch.

**1.9 Design a restaurant ordering system.
You do not need to write code, but describe a high-level approach:
a. Draw a list of key requirements
b. What are your main considerations and problems?
c. What components or tools would you potentially use?**

a. Some of the requirements to consider could be:

- Menu creation and management: how can the menu be created, managed and edited by staff members
- Placing orders: orders placed only by staff or could we have an option for customers to place orders?
- Tracking orders: system should be able to show list of orders, progress of current orders, order history, etc.
- Management of payments: using a POS system, handle, manage and keep track of payments

b. Main considerations and problems:

- Data backup: should have a system for backing up data so that data is not lost in case of system issues/accidental damage
- UI/UX considerations: How tech-savvy does someone need to be to use the system? It should be simple for the average person to utilise and come with instructions for use. Can it be used by differently-abled users? Can the users customise/edit the system? etc.
- Offline availability: can the system be used if there is no internet connection, in case of power outage? How can we minimise disruption of service in such occurrences?

c. Components and tools to use:

- Use of an appealing and user-friendly interface, utilising front-end technologies to handle client-side of system
- Use of back-end technologies (like Python) to handle server-side of the system
- Use of a database (like MySQL) to keep track of orders, payments, customer information, etc.
- POS system for efficient and effective management of payments
- Use of a method to backup data such as a cloud storage service
