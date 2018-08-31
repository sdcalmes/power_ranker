$(document).ready(function () {
    $('#power_table').DataTable(
			    { "paging": false,
				    "info"  : false,						
					  columnDefs : [
					     { targets:[9],orderData:[9,0]}
				     ],
						 "fnRowCallback": function(nRow, aData, iDisplayIndex, iDisplayIndexFull){
			    				console.log(aData[9]);
								     if( aData[9] == "1"){$('td', nRow).addClass('row-tier1'); } 
								else if( aData[9] == "2"){$('td', nRow).addClass('row-tier2'); } 
								else if( aData[9] == "3"){$('td', nRow).addClass('row-tier3'); } 
								else if( aData[9] == "4"){$('td', nRow).addClass('row-tier4'); } 
								else if( aData[9] == "5"){$('td', nRow).addClass('row-tier5'); } 
						}
		    	}
		);
        $('#projections_table').DataTable(
			    { "paging": false,
				    "info"  : false,
					  columnDefs : [
					     { targets:[5],orderData:[5,0]}
				     ],
						 "fnRowCallback": function(nRow, aData, iDisplayIndex, iDisplayIndexFull){
			    				console.log(aData);
								     if( aData[0] <= "2"){$('td', nRow).addClass('row-tier1'); }
								else if( aData[0] <= "4"){$('td', nRow).addClass('row-tier2'); }
								else if( aData[0] <= "6"){$('td', nRow).addClass('row-tier3'); }
								else if( aData[0] <= "9"){$('td', nRow).addClass('row-tier4'); }
								else if( aData[0] <= "12"){$('td', nRow).addClass('row-tier5'); }
						}
		    	}
		);
});

