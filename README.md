# logsapp

## Project
This is a demonstration on how log you can use sql together with python to look through a quieres of data.

## How to run it.

### What you need:
- Python
- Vagrant
- VirtualBox

## Setup requirements

1. Install Vagrant and VirtualBox.
2.  Clone this repository logsapp(https://github.com/lashleykeith/logsapp).
3. Extract the file newsdata once you have cloned the repository.

## Running the application
Launch Vagrant VM by running `vagrant up`.  Then you can log in with `vagrant ssh`.

If you want ot load the psql file you can use the command `psql -d news -f newsdata.sql`
to connect the the database and run SQL statements.  However you don't need to do this.
You can simply just run the program and the queries unzipping the newsdata.sql file 
and the program will load will load.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run `python3 newsdata.py` from the command line.


4.  You will be prompt to a greeting. The computer tell you to give  the name of a file you want to make.  Itwill look for your files by will also tell you to pick a song title you must do these.

5.  Then you programming will tell you that it is getting some music. After this it will print both the list of the  3 data sets
and make a txt file with the same information.
