#!/bin/sh

DEST=ammapVisitedCountries.js
curl https://www.amcharts.com/lib/3/ammap.js > ${DEST}
curl https://www.amcharts.com/lib/3/maps/js/worldLow.js >> ${DEST}
cat >> ${DEST} <<EOF
  var map = AmCharts.makeChart("mapdiv",{
    type: "map",
    theme: "dark",
    projection: "mercator",
    panEventsEnabled : true,
    backgroundColor : "#FFF",
    backgroundAlpha : 1,
    zoomControl: {
      zoomControlEnabled : true
    },
    dataProvider : {
      map : "worldLow",
      getAreasFromMap : true,
      areas :
        [
        {
          "id": "RU",
          "showAsSelected": true
        },
        {
          "id": "CN",
          "showAsSelected": true
        },
        {
          "id": "MY",
          "showAsSelected": true
        },
        {
          "id": "TH",
          "showAsSelected": true
        },
        {
          "id": "TW",
          "showAsSelected": true
        },
        {
          "id": "HK",
          "showAsSelected": true
        },
        {
          "id": "AU",
          "showAsSelected": true
        }
      ]
    },
    areasSettings : {
      autoZoom : true,
      color : "#B4B4B7",
      colorSolid : "#84ADE9",
      selectedColor : "#84ADE9",
      outlineColor : "#666666",
      rollOverColor : "#9EC2F7",
      rollOverOutlineColor : "#000000"
    }
  });
EOF
