window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        // console.log(target.name); // ID
        // console.log(target.value); // QU
        $.ajax({
            url: '/baskets/edit/' + target.name + '/' + target.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
    });
}