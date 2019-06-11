Welcome To The Barbershop!

1 Introduction

    As a barbershop owner, this app will make the process of choosing a barber much more convenient and efficient for your customers. This
    app was made by a barbershop patron who has experienced the struggles of an inefficiently run shop. The next 2 paragraphs are some anecdotes
    about the true event that happened to me that inspired the creation of this app.

    The first time I went to a barbershop, I did not know how the shop operated. There were multiple barbers cutting hair and everyone who
    was not getting a haircut was sitting along the waiting wall. So naturallly, I walked in and went straight to sit down. However, I was
    unaware that people uually had a specific barber they were waiting for and each barber genrally knew who they were going to cut. So I
    am sitting waiting for my turn but none of the barbers are calling me up because none of them thought I was going to them. If only there
    was a way to sign up for a barber, I would not have sat there uselessly waiting for a barber.

    After coming to this shop for a couple month, I had my established my barber—he knew me and I knew him. One busy Friday afternoon, I
    went to get a cut. I remember I walked in right behind someone I had just seen in the parking lot but they took a shortcut to get to
    the shop before me. Therefore, he would get his cut before I did. Since it was a busy day, I ended up waiting 2+ hours for my turn to
    get cut. After the guy I walked in with had gotten up from my barber's chair, I stood up to get my haircut, but my barber said it was
    not my turn and another guy was before me. I told him that was wrong because I walked in at the same time as the guy whi just got cut.
    My barber wasn't convinced and I was not trying to get into a fight with him before he cut my hair because then he may maliciously
    ruin my hairline. I was about to just take loss until another barber verified that it was my turn.  Again, had there been this app,
    all of that could have been avoided.

2 Setup
    This web app will require a computer or tablet with internet collection as the primary device where patrons will sign up on.
    Additionally, each barber should have a device that connects to the internet like a smartphone (recommended), tablet, or laptop.

    2.1 Running flask
        To run the website, open CS50 ide and ensure that your workspace is in the correct folder (Go to workspace -> project -> barbershop).
        Execute "flask run" in your workspace and follow the link provided to you. In reality, the device requries at least 2 devices,
        so either open the link in an internet browser on another device or for testing purposes only you can open the link in a different
        browser on the same device to simulate multiple devices.

3 Usage
    The way this app works is there is the store front pages which is under the store login. These are the pages that the store uses to
    manage its clients and barbers. It is also where the customers join the queue. Then there is the barber pages under the barber login
    and this where each individual barber can see its own queue.

    3.1 Store Front
        The device for the storefront should be a laptop or tablet with a big enough screen for the customers to easily see and sign up on.

        3.1.1 Register
            Now that you have the browser open on at least 2 different devices, both webpages should be open to a login screen. Firstly, on the
            main device/browser click the register tab to register your barber shop store. Include the name of your Barber shop, choose a username
            and a password, and confirm the password. CLick submit and you should be taken to the home page where you will see "Welcome to 'Name of
            Shop'". If there is an error in the registration (i.e. username not entered or already exists) an error page will pop up pointing towards
            the error.

        3.1.2 Login
            Once a store has been registered, it can access its pages by logging in under "Store Login". Provide the username and passwoord
            that was created during registration to access.

        3.1.3 Home
            If the registration is successful, you will be redirected to the home page. The home page will display all of your barbers information
            and is the site that all the customers will first see and interact with upon arriving to the shop. Click the "Create Barber" button to
            be taken to the "Create Barber page" and add barbers to your site. After you create barbers they will appear as cards on the home page.
            The reset button at the buttom of the page is used to clear the entire queue of every barber. It will delete every customer that signed up
            and reset the wait time to 0. Only use if you need to clear everything.

        3.1.4 Create Barber
            The create barber page is where you will add barbers to your database. It is a simple form where you fill out the barber's name and their
            chair number (i.e. 1st chair "1", 2nd chair "2") so that customers can identify who they sign up to. After creating a barber, submit the
            information and you will be redirected back to the home page after a verification "added" page.

        3.1.5 Get ID
            Once you create a barber, they are assigned a unique id in the database. This ID will be used to log them into their individual barber
            login. Also, when a store is registered, the store is assigned a unique store id. All of this information can be found in the Get ID page
            which you access by clicking the "Get ID" tab in the navigation bar.

        3.1.6 Choose
            The choose page is where customers can select which barber they want and add their names to the queue. There are 2 different ways to get
            to this page: 1) Clicking the "Choose" tab in the navigation bar at the top of the page or 2) clicking select barber at the bottom of each
            barber's card. Once on the choose page, the cutomer will select which barber they want and write their name to be added to the queue.

        3.1.7 Logout
            By clicking the logout tab in the navigation bar, the user will logout of the store web pages.

    3.2 Barber Pages
        Use a separate device to open the barber pages. In reality it could be a cell phone or small tablet that the barber keeps for themself. 
        For testing purposes only, you can use the same device used for the store front pages but you must use a different browser to simulate different devices.

        3.2.1 Login
            No registration is necessary to log into the barber pages because the barber is "registered" when they are created in the store.
            To log in, go to the "Barber Login" from the login page and enter the barber's name (as written in the Barber ID), and the Barber
            ID and Store ID. After submitting the info, you will be redirected to the Barber home page. If anything is enetered incorrectly,
            an error message will pop up pointing to the error.

        3.2.2 Home
            The barber home page will display the first 2 people in the queue. Thus will allow the barber to know who is going to be cut and
            who will be next. This is the only page in the barber side.  As people sign up on the store pages, the names will begin to appear
            on the barber home. Click the "Refresh" tab in the navigation bar to update the barber page. When the barber is finished cutting the
            current customer's hair, click the "Finished" button. This will remove that customer from the queue, update the next 2 spots, and edit
            the waiting time on the store home for that barber.

        3.2.3 Logout
            By clicking the logout tab in the navigation bar, the user will logout of the barber web pages.