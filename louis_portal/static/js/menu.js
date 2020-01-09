(function () {
    'use strict';

    // page constants
    var menuSlideTime = 120;

    function $menuItem($elem) {
        var item = $elem.attr('data-sub');
        return $('#' + item);
    }

    function $parentMenu($elem) {
        return $('.nav-menu-item[data-sub="' + $elem.prop('id') + '"]');
    }

    function showMenuDrop($elem) {
        $menuItem($elem).slideDown(menuSlideTime);
    }
    function hideMenuDrop($elem) {
        $menuItem($elem).slideUp(menuSlideTime);
    }

    $('.nav-menu-item').on('mouseenter', function () {
        $('.nav-menu-item').not($(this)).each(function() {
            hideMenuDrop($(this));
        })
        showMenuDrop($(this));
    });

    $('.sub-menu').on('mouseleave', function () {
        hideMenuDrop($parentMenu($(this)));
    });
})();