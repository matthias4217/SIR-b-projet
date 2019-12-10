/**
 * Script using JQuery
 */


/**
 *
 * @param cookies: int
 */
function update_cookies_nbr(cookies) {
    $("#cookies_number").text(cookies);
}


/**
 *
 * @param upgrades
 */
function update_upgrades(upgrades) {
    // upgrade stuff to buy #upgrades
    // we'll assume no upgrades have been added
    $(".upgrade-sold").each(function( index ) {
        //console.log( index + ": " + $( this ).text() );
        $(this).text("<div>" + upgrades[index]["name"] + " : " + upgrades[index]["base_cost"]
            + " cookies\n</div><small><font color=\"grey\"></small>" + upgrades[index]["cpc"]
        + " per click each</font>\n</small>");
    });

    $(".upgrade-bought").each(function( index ) {
        //console.log(upgrades[index]["name"] + " : " + upgrades[index]["number"]);
        $(this).text(upgrades[index]["name"] + " : " + upgrades[index]["number"]);
    });
    // upgrade stuff owned  #list
}

/**
 * Get the suggested tracks
 */
function refresh_gamedata() {
    $.get("/refresh", function (data) {
        let cookies_nbr = data.cookies;
        let upgrades = data.upgrades;
        update_cookies_nbr(cookies_nbr);
        update_upgrades(upgrades);
    });
}

setInterval(refresh_gamedata, 1000);