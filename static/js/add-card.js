$(document).ready(function () {
  // Define cardRow as a jQuery object
  var cardRow = $("#cardRow");

  // When the "Add Card" button is clicked
  $("#addCardBtn").click(function () {
    // Get the name entered by the user
    var name = $("#recipient-name").val();

    // Create a Bootstrap card with the entered name
    var card =
      '<div class="col-md-4">' +
      '<div class="card">' +
      '<div class="card-body">' +
      '<h5 class="card-title">' +
      name +
      "</h5>" +
      '<p class="card-text"><strong>Balance:</strong> $45</p>' +
      '<button class="btn btn-primary btn-sm">Send Transactions</button>' + // Add a button to the card
      "</div>" +
      "</div>" +
      "</div>";

    // Append the card to the cardRow
    cardRow.append(card);

    // Hide the modal popup
    $("#exampleModal").modal("hide");

    // Reset the form
    $("#recipient-name").val("");

    // Add a click event listener to the button in the new card
    cardRow.find(".card-body:last button").click(function () {
      alert("You clicked the button in the card with title: " + name);
    });
  });
});
