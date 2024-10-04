
//                              settings dropdown
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.settings-btn').addEventListener('click', function () {
        var dropdownContent = document.querySelector('.dropdown-content');
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
            settingsItem.classList.remove('active');
        }
    });
});

//                                         search result

function showResults() {
    var query = document.querySelector('input[name="search"]').value;
    var resultsContainer = document.getElementById('search-results');

    if (query.length > 0) {
        resultsContainer.style.display = 'block';
    } else {
        resultsContainer.style.display = 'none';
    }
}

document.addEventListener('click', function (event) {
    var resultsContainer = document.getElementById('search-results');
    if (!event.target.closest('.search-bar')) {
        resultsContainer.style.display = 'none';
    }
});



//                                   Comment toggle
function toggleCommentBox(postId) {
    var commentBox = document.getElementById('comment-box-' + postId);
    if (commentBox.style.display === 'none' || commentBox.style.display === '') {
        commentBox.style.display = 'block';
    } else {
        commentBox.style.display = 'none';
    }
}