document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript is working!');
    
    const posts = document.querySelectorAll('.post-grid ');

    posts.forEach(post => {
        const image = post.querySelector('.post-image');
        const overlay = post.querySelector('.post-overlay');

        image.addEventListener('mouseover', () => {
            overlay.style.display = 'block';
        });

        image.addEventListener('mouseout', () => {
            overlay.style.display = 'none';
        });
    });
});


