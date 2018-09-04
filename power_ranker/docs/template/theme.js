$(document).ready(function () {
    $('#power_table').DataTable(
			    { "paging": false,
				    "info"  : false,
					  columnDefs : [
					     { targets:[10],orderData:[10,0]}
				     ],
						 "fnRowCallback": function(nRow, aData, iDisplayIndex, iDisplayIndexFull){
								     if( aData[10] == "1"){$('td', nRow).addClass('row-tier1'); }
								else if( aData[10] == "2"){$('td', nRow).addClass('row-tier2'); }
								else if( aData[10] == "3"){$('td', nRow).addClass('row-tier3'); }
								else if( aData[10] == "4"){$('td', nRow).addClass('row-tier4'); }
								else if( aData[10] == "5"){$('td', nRow).addClass('row-tier5'); }
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
								     if( aData[0] <= "2"){$('td', nRow).addClass('row-tier1'); }
								else if( aData[0] <= "4"){$('td', nRow).addClass('row-tier2'); }
								else if( aData[0] <= "6"){$('td', nRow).addClass('row-tier3'); }
								else if( aData[0] <= "9"){$('td', nRow).addClass('row-tier4'); }
								else if( aData[0] <= "12"){$('td', nRow).addClass('row-tier5'); }
						}
		    	}
		);
});

