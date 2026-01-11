// sidebar
let navToggle = document.querySelector('#navToggle');
let sideNav = document.querySelector('#side-nav');
let closeNav = document.querySelector('#closeNav');
navToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    sideNav.style.right = "0";
    sideNav.style.opacity = "1";
});
closeNav.addEventListener("click", (e) => {
    e.stopPropagation(); 
    sideNav.style.right = "-100%";
    sideNav.style.opacity = "0";
});
document.addEventListener("click", () => {
    sideNav.style.right = "-100%";
    sideNav.style.opacity = "0";
});
// services animation 
let mouse = document.querySelector(".mouse");
let service = document.querySelector('.services');
// mouse animation 
    mouse.style.width = '20px';
    mouse.style.height = '20px';
    mouse.style.borderRadius = '20px';
    mouse.style.position = 'absolute';
    mouse.style.zIndex = '5';
service.addEventListener("mousemove", (ang) => {
    let rect = service.getBoundingClientRect();
    gsap.to(mouse, {
        x: ang.clientX - rect.left,
        y: ang.clientY - rect.top,
        duration: 0.3,
        ease: "none"
    });
});
// cards animation 
service.addEventListener("mousemove",(angel) =>{
    let max = 60;
    let angX = ((angel.clientY / window.innerWidth) - 0.5) * max * 2;
    let angY = ((angel.clientX / window.innerWidth) - 0.5) * max * 2;
    gsap.to(".service-card",{
        rotateY: angY,
        rotateX: -angX,
        duration: 0.3,
        ease: "power3.out reverse"
    })
});
service.addEventListener("mouseleave",(an)=>{
    gsap.to(".service-card",{
        rotateY: 0,
        rotateX: 0,
        duration: 0.3,
        ease: "power3.out reverse"
    });
});
// projects cards
let pro_card = document.querySelectorAll("#project-card");
pro_card.forEach(pro_card => {
    pro_card.addEventListener("mousemove",(angel) =>{
        let max = 30;
        let angX = ((angel.clientY / window.innerWidth) - 0.5) * max * 2;
        let angY = ((angel.clientX / window.innerWidth) - 0.5) * max * 2;
        gsap.to(pro_card,{
            rotateY: angY,
            rotateX: -angX,
            duration: 0.8,
            ease: "power3.out reverse"
        })
    });
    pro_card.addEventListener("mouseleave",(an)=>{
        gsap.to(pro_card,{
            rotateY: 0,
            rotateX: 0,
            duration: 0.8,
            ease: "power3.out reverse"
        });
    });
});
// GSAP Animations 
 gsap.from("#hero-img",{
     x: 800,
    y:-500,
    delay:0.5,
    duration:1,
});
gsap.from('#hero-h2',{
    x: -500,
    delay: 0.5,
    duration:1,
});
gsap.from('#hero-h1',{
    y:100,
    delay:0.5,
    duration:1,
    opacity:0,
});