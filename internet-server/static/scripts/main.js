/**
 * Script using JQuery
 */


/**
 *
 * @param cookies: int
 */
function update_cookies_nbr(cookies) {
    $("#cookies_number").text(cookies.toFixed(2));
}


function update_selection(selection_id) {
    $(".upgrade-sold").removeClass("active");
    $(".upgrade-sold").addClass("inactive");
    $(".upgrade-sold").each(function(index) {
        console.log("Index : " + index + "; Id : " + selection_id);
        if (index === selection_id)
        {
            $(this).addClass("active");
        }
    })
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
        $(this).find("div").text(upgrades[index]["name"] + " : " + (upgrades[index]["base_cost"] *1.1**upgrades[index]["number"]).toFixed(2)
            + " cookies\n");
        $(this).find("small").text(upgrades[index]["cpc"].toFixed(2) + " cookies per click each");
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
        update_selection(data.selection_id);
    });
}

function click_cookies() {
    $.get("/click");
}

$("#click-button").click(click_cookies);

setInterval(refresh_gamedata, 100);
