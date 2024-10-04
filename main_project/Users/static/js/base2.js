document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.querySelector('.sidebar-item.dropdown');
    const dropdownContent = document.querySelector('.dropdown-content');

    dropdown.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent clicks from bubbling up
        const isVisible = dropdownContent.style.display === 'block';
        dropdownContent.style.display = isVisible ? 'none' : 'block';
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
        if (!dropdown.contains(event.target) && !dropdownContent.contains(event.target)) {
            dropdownContent.style.display = 'none';
        }
    });
});

// document.addEventListener('DOMContentLoaded', function() {
//     const searchBox = document.querySelector('.search-box');
//     const searchResults = document.getElementById('search-results');

//     // Show the search results if there are any users
//     if (searchResults.children.length > 0) {
//         searchResults.style.display = 'block';
//     }

//     // Close search results when clicking outside
//     document.addEventListener('click', function(event) {
//         if (!searchBox.contains(event.target) && !searchResults.contains(event.target)) {
//             searchResults.style.display = 'none';
//         }
//     });

//     // Prevent form submission when pressing Enter
//     searchBox.addEventListener('keydown', function(event) {
//         if (event.key === 'Enter') {
//             event.preventDefault(); // Prevent form submission
//         }
//     });
// });

function toggleCommentBox(postId) {
    var commentBox = document.getElementById('comment-box-' + postId);
    if (commentBox.style.display === 'none' || commentBox.style.display === '') {
        commentBox.style.display = 'block';
    } else {
        commentBox.style.display = 'none';
    }
}