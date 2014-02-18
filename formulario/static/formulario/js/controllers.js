var formUserApp = angular.module('formUserApp', [])

formUserApp.config(function($interpolateProvider) {
	  $interpolateProvider.startSymbol('{[{');
	  $interpolateProvider.endSymbol('}]}');
	});

formUserApp.controller('StarListCtrl', function ($scope){
	$scope.stars = [
	    {'name': 'Joaquim Phoenix',
	    'snippet': 'Ator'},
	    
	    {'name': 'Bruce',
	    'snippet': 'Cantor'},
	    
	    {'name': 'Neymar',
	    'snippet': 'Jogador'},
    ];
});