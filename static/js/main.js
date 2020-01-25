// Login-register forms
function openCloseContainer(openButtonClass, closeButtonClass, containerClass, showClass) {
    let openButton = document.querySelector(openButtonClass)
    let closeButton = document.querySelector(closeButtonClass)
    let container = document.querySelector(containerClass)

    if (openButton !== null) {
        openButton.addEventListener('click', () => {
            container.classList.toggle(showClass)
        })
        closeButton.addEventListener('click', () => {
            container.classList.toggle(showClass)
        })
    }
}

openCloseContainer('.login-register-button', '.close-forms-button', '.login-register-forms', 'show')

openCloseContainer('.show-contact-form-button', '.close-contact-form-button', '.contact-form-container', 'show')

openCloseContainer('.open-update-post-form-button', '.close-update-post-form-button', '.update-post-form', 'show')

openCloseContainer('.open-delete-post-form-button', '.close-delete-post-form-button', '.delete-post-form', 'show')
openCloseContainer('.open-add-post-form', '.close-add-post-form', '.create-post-form', 'show')

let openEditButtons = document.querySelectorAll('.open-edit-comment')
let closeEditButtons = document.querySelectorAll('.close-edit-comment-form')
let openDeleteButtons = document.querySelectorAll('.open-delete-comment')
let closeDeleteButtons = document.querySelectorAll('.close-delete-comment-form')

openEditButtons.forEach(openButton => {
    openButton.addEventListener('click', (event) => {
        let editCommentForm = event.target.parentElement.querySelector('.edit-comment-form');
        editCommentForm.classList.toggle('show')
    })
})

closeEditButtons.forEach(openButton => {
    openButton.addEventListener('click', (event) => {
        let editCommentForm = event.target.parentElement;
        editCommentForm.classList.toggle('show')
    })
})

openDeleteButtons.forEach(openButton => {
    openButton.addEventListener('click', (event) => {
        let deleteCommentForm = event.target.parentElement.querySelector('.delete-comment-form')
        deleteCommentForm.classList.toggle('show')
    })
})
closeDeleteButtons.forEach(closeButton => {
    closeButton.addEventListener('click', (event) => {
        let deleteCommentForm = event.target.parentElement
        deleteCommentForm.classList.toggle('show')
    })
})