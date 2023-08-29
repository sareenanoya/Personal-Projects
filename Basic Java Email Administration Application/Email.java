package emailapp;

import java.util.Scanner;

//personal project
//Basic Email Administration Application

public class Email {
    private String firstname;
    private String lastname;
    private String password;
    private String email;
    private String department;
    private int mailboxCapacity = 500;
    private int defaultPassLength = 10;
    private String alternateEmail;
    private String companySuffix = "sareenacompany.com";

    // need constructor to receive first and last name
    public Email(String firstname, String lastname){
        this.firstname = firstname;
        this.lastname = lastname;
        System.out.println("New Worker: " + this.firstname + " "+ this.lastname);

        this.department = setDepartment();
       // System.out.println("Department: " + this.department);

        //call a method that returns a random password
        this.password = randomPassword(defaultPassLength);
        System.out.println("Your password is: "+ this.password);

        // combine elements to generate email
        email = firstname.toLowerCase() + "." + lastname.toLowerCase() + "@" + department + "."+ companySuffix;
        System.out.println("Your email is: " + email);
    }

    //ask for department
    private String setDepartment(){
        System.out.print("Department Codes: \n1 for Sales\n2 for Development\n3 for Accounting\n0 for none\nEnter Department code: ");
        Scanner in = new Scanner(System.in);
        int depChoice = in.nextInt();
        if (depChoice == 1){return "sales";}
        else if (depChoice == 2){return "dev";}
        else if (depChoice == 3){return "acct";}
        else {return "";}
        }


    // generate a random password
    private String randomPassword(int length){
        String passwordSet = "aqwertyuiopasdfghjklzxcvbnm1234567890?!@%$";
        char[] password = new char[length];
        for (int i = 0; i<length; i++) {
            int rand = (int) (Math.random() * passwordSet.length());
            password[i] = passwordSet.charAt(rand);
        }
        return new String(password);
    }
    // set the mailbox capacity
    public void setMailboxCapacity(int capacity){
        this.mailboxCapacity = capacity;
    }
    // set the alternate email
    public void setAltEmail(String altmail){
        this.alternateEmail = altmail;
    }
    // change the password
    public void changePass(String password){
        this.password = password;
    }
    public int getMailboxCapacity(){ return mailboxCapacity; }
    public String getAlternateEmail(){ return alternateEmail; }
    public String getPassword() { return password; }

}


