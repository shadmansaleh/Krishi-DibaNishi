document.querySelectorAll(".tab").forEach((tab) => {
    tab.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach((btn) => btn.classList.remove("active"));
      document.querySelectorAll(".tab-content").forEach((content) => content.classList.add("hidden"));
  
      tab.classList.add("active");
      document.getElementById(`${tab.id.split("-")[0]}-section`).classList.remove("hidden");
    });
  });
  
 
  
  let articles = [];
document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((btn) => btn.classList.remove("active"));
    document.querySelectorAll(".tab-content").forEach((content) => content.classList.add("hidden"));

    tab.classList.add("active");
    document.getElementById(`${tab.id.split("-")[0]}-section`).classList.remove("hidden");
  });
});

// Ensure the DOM content is loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Select all FAQ questions
    const faqQuestions = document.querySelectorAll('.faq-question');
  
    // Add click event listeners to each FAQ question
    faqQuestions.forEach((question) => {
      question.addEventListener('click', () => {
        const answer = question.nextElementSibling; // Find the corresponding answer
  
        // Toggle the 'hidden' class to show or hide the answer
        if (answer.classList.contains('hidden')) {
          answer.classList.remove('hidden'); // Show the answer
        } else {
          answer.classList.add('hidden'); // Hide the answer
        }
      });
    });
  });
  
  


const articleForm = document.getElementById("article-form");
const latestArticlesContainer = document.getElementById("latest-articles");

function updateLatestArticles() {
  latestArticlesContainer.innerHTML = "";
  const latestArticles = articles.slice(-5).reverse();
  latestArticles.forEach((article) => {
    const articleCard = `
      <div class="card">
        <h3>${article.title}</h3>
        <p>${article.content}</p>
        <small>By ${article.author}</small>
      </div>
    `;
    latestArticlesContainer.innerHTML += articleCard;
  });
}
const problemForm = document.getElementById("problem-form");
const problemResponse = document.getElementById("problem-response");
const responseMessage = document.getElementById("response-message");

problemForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Get the user's input
  const problemDescription = document.getElementById("problem-description").value;

  // Generate a basic response based on the input
  let response = "We recommend performing a soil test to analyze its pH and nutrient levels.";
  if (problemDescription.toLowerCase().includes("acidic")) {
    response = "To address acidic soil, consider adding lime to neutralize the pH.";
  } else if (problemDescription.toLowerCase().includes("low fertility")) {
    response = "For low fertility, incorporate organic matter such as compost or manure.";
  } else if (problemDescription.toLowerCase().includes("salty")) {
    response = "For saline soil, improve drainage and consider using gypsum.";
  }

  // Display the response
  responseMessage.textContent = response;
  problemResponse.classList.remove("hidden");

  // Clear the form
  problemForm.reset();
});


articleForm.addEventListener("submit", (e) => {
    e.preventDefault();
  
    // Collect form data
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;
    const author = document.getElementById("author").value;
  
    // Add the new article to the articles array
    articles.push({ title, content, author });
  
    // Update the UI with the latest articles
    updateLatestArticles();
  
    // Clear the form
    articleForm.reset();
  });
  

    