Part A — Setup & First Run (5 minutes)

Open exercise.html in your browser.
Open Developer Tools → Console (Chrome: F12).
Click the buttons in this order:
Async Timeout
Async Promise
Async Await
Async Fetch
✅ Checkpoint (write down in your notebook):

What do you see in the output for Timeout? 
Status: Idle

Start
End
Timeout finished after 0.5 seconds
What does the Status line show for Promise/Await/Fetch?
 Status: Idle

Promise resolved after 1 second!
Status: Idle

Before await
After await
Promise resolved after 1 second!
Status: Idle

Error: HTTP Error: 404



Part B — Timeout

What changed?
→ The delay became shorter (0.5 seconds instead of 2 seconds)

Did “End” appear before timeout?
→ Yes

Why?
Because the delay is controlled by setTimeout, not by the message text.
 
  Part C
  Did the button click freeze the page?
  No, the page did not freeze because Promises are asynchronous.

When does .then() run?
.then executes after the Promise completes (resolves).
The message text is just a string; the real delay is controlled by setTimeout. They don’t have to match — this shows that the .then waits for the actual Promise to resolve, not for the message text.


Part D

What does await do?
 It pauses the function until the Promise finishes, without blocking the browser.pauses the async function until the Promise resolves, then execution continues with the next lines.
 
 What is the order of the three logs?
 "Before await" prints immediately.

await pauses the function until the Promise resolves (2 seconds in your modified code).

"After await" prints next, followed by the resolved value of the Promise ("Promise resolved after 1 second!").

This shows that await pauses the function but does not freeze the browser.

Part E — Fetch

What message appears?
 Error: HTTP Error: 404

 1️ Why do we use async/await?

Answer:
We use async/await to write asynchronous code in a way that looks like normal, synchronous code. It makes Promises easier to read and reason about, especially when we have multiple asynchronous operations.

2️ Why do we use try/catch with fetch?

Answer:
We use try/catch to handle errors, such as network failures or manually thrown errors. This prevents the program from crashing and allows us to display a meaningful message when something goes wrong.

3️ Why do we check response.ok?

Answer:
fetch does not automatically throw an error for HTTP errors (like 404 or 500). Checking response.ok ensures we detect failed requests and handle them properly.

Why check response.ok?
 Because fetch does not throw errors for HTTP problems automatically.
 
 1. Why do we use async/await?

Async/await makes asynchronous code easier to read and write. It allows us to write code that looks synchronous while still handling asynchronous operations like API calls.

2. Why do we use try/catch with fetch?

We use try/catch to handle errors such as network failures or manually thrown errors. It prevents the program from crashing and allows us to show error messages.

3. Why do we check response.ok?

Because fetch does not automatically fail on HTTP errors like 404 or 500. We check response.ok to detect these errors and handle them properly.
