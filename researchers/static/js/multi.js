function keep (target) {
    console.log(target, $(target).offset());
    console.log( $(target).offset().top - 140 );
    window.scrollTo(0, $(target).offset().top - 140);

    $('#search').val('');
    $('.suggestions').html('');

    setTimeout(()=>console.log( window.scrollY ), 1000);
};
