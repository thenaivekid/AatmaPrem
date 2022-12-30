var menu = document.getElementById("navlink");
const openmenu = () => {
  console.log(menu.className);
  if (menu.className === "navlink") {
    menu.className = "menuresponsive";
  } else {
    menu.className = "navlink";
  }
};


