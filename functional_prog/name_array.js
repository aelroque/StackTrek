
const users = [
    { firstName: "Susan", lastName: "Steward" },
    { firstName: "Daniel", lastName: "Longbottom" },
    { firstName: "Jacob", lastName: "Black" },
  ];
  let fullUserNames;
  
  fullUserNames = users
  .map(users => `${users.firstName} ${users.lastName}`);
  console.log(fullUserNames);

  //name