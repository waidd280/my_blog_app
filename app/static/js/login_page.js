function greet(){
    alert("Welcome to BlogApp");
}

function checkEntry(){
    var email, password;

    email = document.getElementById("email_entry").value;
    password = document.getElementById("password_entry").value;

    if (email === "" || password === ""){
        alert("All fields must be filled");
    }
}

function must_login(){
    alert("You must log in to post a question");
}