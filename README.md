Set Up:

-> A folder named 'ATM Files', must exist at the same level (same place) where this program is stored.

-> 'ATM Files' must contain at least one (non empty) text file, containing the records/data.

-> Each record in a file must be in the specified format. Records are seperated by newline '\n'.

-> Format:

   {AccountNumber},{BranchCode},{HolderName},{CurrentBalance},{WithdrawalLimit},{Pin},

-> A sample data file has been provided.


Usage:


-> This program is designed to handle multiple files.

-> Here is a list of valid operation codes that can be entered and their use:

     - help
     (to display list of normal operations)
     
     - wth
     (to withdraw amount)
     
     - dep
     (to deposit amount)
     
     - chk
     (to display account details)
     
     - showall
     (to show all records in a particular file)
     
     - sysexit
     (to exit/end program)

-> The 'showall' operation will ask for a pin, which is assigned to the variable 'adminpass' (current pin = 25807)

-> The program will keep running the loop untill you enter, 'sysexit'
