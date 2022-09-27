const courseLogoUpload = document.querySelector("#id_course_logo");
const courseLogoImg = document.querySelector("#id_logo_img");
const courseProfileUpload = document.querySelector("#id_course_profile");
const courseProfileImg = document.querySelector("#id_profile_img");
const eventImgUpload = document.querySelector("#id_photo");
const eventImg = document.querySelector("#id_event_img");
const eventNewImgUpload = document.querySelector("#div_id_photo #id_photo");
const eventNewImg = document.querySelector("#id_event_new_img");
const updateCourseLogoUpload = document.querySelector(
  "#div_id_course_logo #id_course_logo"
);
const updateCourseLogoImg = document.querySelector("#updatecourse_new_logo");
const updateCourseProfileUpload = document.querySelector(
  "#div_id_course_profile #id_course_profile"
);
const updateCourseProfileImg = document.querySelector("#updatecourse_new_img");

// blog img preview

const updateBlogImg = document.querySelector("#div_id_photo #id_photo");
const updateBlogImgPrev = document.querySelector("#blog_img_preview");
console.log(updateBlogImg);

const onChangeImage = (input, img) => {
  if (input && img) {
    input.addEventListener("change", () => {
      const [file] = input.files;
      if (file) {
        img.src = URL.createObjectURL(file);
      }
    });
  }
};

onChangeImage(courseLogoUpload, courseLogoImg);
onChangeImage(courseProfileUpload, courseProfileImg);
onChangeImage(eventImgUpload, eventImg);
onChangeImage(eventNewImgUpload, eventNewImg);
onChangeImage(updateCourseLogoUpload, updateCourseLogoImg);
onChangeImage(updateCourseProfileUpload, updateCourseProfileImg);
onChangeImage(updateBlogImg, updateBlogImgPrev);

// accordion
const openIcon1 = document.getElementById("accordion-open1");
const accordionBtn1 = document.querySelector("#accordion-button1");
const openIcon2 = document.getElementById("accordion-open2");
const accordionBtn2 = document.querySelector("#accordion-button2");

accordionBtn1?.addEventListener("click", () => {
  openIcon1.classList.toggle("show-accordion");
});
accordionBtn2?.addEventListener("click", () => {
  openIcon2.classList.toggle("show-accordion");
});

//show password
const loginInput = document.querySelector(" #id_password");
const loginIcon = document.querySelector(" #togglePassword");
console.log(loginIcon);

loginIcon.addEventListener("click", () => {
  const type =
    loginInput.getAttribute("type") === "password" ? "text" : "password";
  loginInput.setAttribute("type", type);
  loginIcon.classList.toggle("fa-eye");
});
