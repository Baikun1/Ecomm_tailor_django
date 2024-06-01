<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>project portfolio</title>
    <script src="https://kit.fontawesome.com/7226ead90d.js" crossorigin="anonymous"></script>
    <!-- <script src="https://kit.fontawesome.com/7226ead90d.js" crossorigin="anonymous"></script> -->
    <link rel="stylesheet" href="index.css">

</head>

<body>


    <div class="nav1">
        <div class="navbar">



            <div class="logo">
                <div class="logolintap">


                    <i class="fa-solid fa-feather-pointed"></i>Baikuntha
                </div>
            </div>


            <div class="serch">
                <a href="">Feature</a>
                <a href="">Pricing</a>
                <a href="">FAQ</a>
                <a href="">Support</a>

            </div>

        </div>

    </div>

    <div class="firstpage">
        <div class="header">

            <div class="midl">
                <div class="mid" id="home">
                    <h6> <a href="C:\xampp\htdocs\c_baikuntha\index.php"><i class="fa-solid fa-house"></i>Home</a></h6>
                </div>
                <div class="mid" id="page">
                    <h6><a href="page.html"><i class="fa-solid fa-hippo"></i>Page</a></h6>
                </div>
                <div class="mid" id="portfolio">
                    <h6> <a href="portfolio.html">Portfolioe</a> </h6>
                </div>
                <div class="mid" id="blog">
                    <h6> <a href="blog.html">Blog</a></h6>
                </div>
                <div class="mid" id="shope">
                    <h6> <a href="shop.html">Shop</a></h6>
                </div>
                <div class="mid" id="Element">
                    <h6> <a href="element.html">Element</a></h6>
                </div>
            </div>
            <!-- <div class="end">
                <i class="fa-solid fa-cart-shopping"></i>
                <i class="fa-solid fa-magnifying-glass"></i>

                <i class="fa-solid fa-braille"></i>

            </div> -->

        </div>



    </div>
<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','db_contact');

// get the post records
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];
$txtPhone = $_POST['txtPhone'];
$txtMessage = $_POST['txtMessage'];

// database insert SQL code
$sql = "INSERT INTO `tbl_contact` (`Id`, `fldName`, `fldEmail`, `fldPhone`, `fldMessage`) VALUES ('0', '$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "<h1>Contact Records Inserted</h1>";
}

?>











<div class="lastpage6">
	
        <div class="twiter">
            <i class="fa-brands fa-facebook"></i>
            <i class="fa-brands fa-linkedin"></i>
            <i class="fa-brands fa-instagram"></i>
            <i class="fa-brands fa-github"></i>
            <i class="fa-brands fa-twitter"></i><br>

        </div>
        Copyright 2023,baikuntha ltd | Privacy Policy
    </div>