I used the basic structure of Finance to build off of for this website.

I have 3 databases that hold all of the information:

Owners:                Barbers:                   Queue:
id                     id                         id
shop name              name                       barber id
username               store id                   client
password               chair number               time
                       wait                       store id

When someone registers a store, they are creating a new owner row. When a new barber is created, a new bareber is created inthe database.
When a customer adds their name and chooses a barber, they create a new queue row. I chose these three because these are the 3 main components
of the entire system: the store, barbers, and customers. I included the store id in both barbers and queue, and the barber id in queue
in order to be able to link all three elements together.

Home.html
    I used html cards to display the informaton of each barber beause it was an efficient and organized way to display the data
    per person in an organized manner. I used jinja loops in the html to add each card to the page. I worte a scipt that automatically
    updates the home page every 3 seconds in order to retrieve the current wait time. Whenever the barber clicks the finshed button,
    the client is removed from the queue and the time is updated. By refreshing every 3 seconds, I can update the wait time on the home
    page.

Added.html
    I included an added page after the creation of a new barber or adding a name to the queue for 2 reasons. For one, it confirms to the user
    that they were indeed added. Secondly, because the pages refresh in order to act accordingly, if someone were to add a new barber or client
    and then immediately refresh, it would resubmit that form and add multiples.

Choose.html
    I used a dropdown for the barber names so that customers can easily select their babrber without having to spell their name. Tis
    allows me to avoid mispelling which would not be read by the program and they would not be added to the queue. I used a jinja loop
    in the html to add the names to the dropdown.

