pragma solidity >= 0.8.11 <= 0.8.11;

contract SmartContract {
    string public userdetails;
    string public tips;   
       
    //call this function to register user details data to Blockchain
    function setSignup(string memory ud) public {
       userdetails = ud;	
    }
   //get register details
    function getSignup() public view returns (string memory) {
        return userdetails;
    }

    //call this function to save tips in Blockchain
    function setTips(string memory t) public {
      tips = t;	
    }
   //get tip details
    function getTips() public view returns (string memory) {
        return tips;
    }
    
   constructor() public {
        userdetails="";
	tips="";
    }
}