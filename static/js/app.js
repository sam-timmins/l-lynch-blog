const copyrightYearRef = document.querySelector("#copyright-year");

// Auto increment of the year in footer
const getFullYear = () =>
  (copyrightYearRef.innerHTML = new Date().getFullYear());

getFullYear();


$(document).ready(function () {
  // Bootstrap
  // Show the toasts
  $(".toast").toast('show');

});