const subscribeForm = document.getElementById("subscribeForm");
const eventForm = document.getElementById("eventForm");

const eventsContainer = document.getElementById("eventsContainer");



async function loadEvents(){

    const response = await fetch("events.json");
    const events = await response.json();

    eventsContainer.innerHTML = "";

    events.forEach(event => {

        eventsContainer.innerHTML += `
            <div class="event">
                <h3>${event.title}</h3>
                <p class="event-date">${event.date}</p>
                <p>${event.description}</p>
            </div>
        `;
    });
}

loadEvents();



subscribeForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const email = document.getElementById("email").value;

    try{

        await fetch(
            "https://560f2burba.execute-api.ap-south-1.amazonaws.com/subscribe",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    email:email
                })
            }
        );

        document.getElementById("subscribeMessage").textContent =
            "Subscription request sent! Check your email.";

        subscribeForm.reset();

    }catch(error){

        document.getElementById("subscribeMessage").textContent =
            "Error subscribing.";

    }

});



eventForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const title =
        document.getElementById("eventTitle").value;

    const date =
        document.getElementById("eventDate").value;

    const description =
        document.getElementById("eventDescription").value;

    try{

        await fetch(
            "https://560f2burba.execute-api.ap-south-1.amazonaws.com/create-event",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    title,
                    date,
                    description
                })
            }
        );

        document.getElementById("eventMessage").textContent =
            "Event created successfully.";

        eventForm.reset();

        loadEvents();

    }catch(error){

        document.getElementById("eventMessage").textContent =
            "Error creating event.";

    }

});
