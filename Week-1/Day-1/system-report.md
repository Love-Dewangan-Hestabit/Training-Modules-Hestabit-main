**Day 1** - **System reverse engineering + Node & Terminal Mastering**

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

Aim:

- Master terminal navigation and system inspection   
- Deep understanding of PATH, environment variables, Node runtime

Tasks:  
1. Identify and document: 

- OS version   
  **lsb_release -a**  
  A legacy command from Linux Standard Base (LSB)  
  Designed to give human-readable OS information  
  [![Commands Screenshot](./Commands%20Images/OS%20version%201.png)]
    
  **cat /etc/os-release**  
  Defined by freedesktop.org  
  Acts as the official OS identity card  
  [![Commands Screenshot](./Commands%20Images/OS%20version%202.png)]
    
    
    
- Current shell   
  **echo $SHELL**  
  Shows **default login** shell  
  Set when the user account is created  
  [![Commands Screenshot](./Commands%20Images/Current%20Shell%201.png)] 
    
  **echo $0**  
  Shows the **currently executing** shell  
  Most accurate for interactive sessions  
  [![Commands Screenshot](./Commands%20Images/Current%20Shell%202.png)]  
    
- Node binary path

  **which node**  
  This shows exactly which node executable is being used  
  [![Commands Screenshot](./Commands%20Images/Node%20binary%20path.png)]  

- NPM global installation path   
  **npm root-g**  
  This shows where npm stores global packages on your system.  
  [![Commands Screenshot](./Commands%20Images/NPM%20global%20installation%20path.png)]   
    
- All PATH entries that include "node" or "npm"  
  **echo $PATH | tr ':' '\n'**  
  Shows all PATH entries line by line  
  [![Commands Screenshot](./Commands%20Images/All%20PATH%20entries.png)]
    
  **echo $PATH | tr ':' '\n' | grep -i -E 'node|npm'**  
  Shows all PATH entries that include “node” or “npm”  
  [![Commands Screenshot](./Commands%20Images/All%20PATH%20entries%20with%20node.png)]


**Observation and Learning**  
These commands would be useful for us whenever our machines act differently and have issue related to path.

- This commands will help when we have issue related to OS compatibility or PATH conflicts.  
- This would also help when we would use CI/CD pipelines during our projects just to confirm what we are running on.  
- This would also be helpful while writing the automation scripts in our project

  

