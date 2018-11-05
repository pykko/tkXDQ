#!/usr/bin/env python3
# coding: utf-8

from tkinter import *
from tkinter.messagebox import *

# CONSTANTES

# Dimensions du plateau de jeu
NB_LIGNES = 9
NB_COLONNES = 7

# Largeur/Hauteur d'une case du plateau
D = 51

# Types de terrain
TERRE = 0
EAU = 1
PIEGE_BLANC = 2
PIEGE_NOIR = 3
TANIERE_BLANC = 4
TANIERE_NOIR = 5

# Directions
NORD = 0
EST = 1
SUD = 2
OUEST = 3


# VARIABLES GLOBALES du Jeu

# Représentation mémoire du plateau de jeu (9 x 7 cases : Tuple de tuples qui peut-être vu comme un tableau 2 dimensions)
jungle = (
		( TERRE , TERRE , PIEGE_NOIR , TANIERE_NOIR , PIEGE_NOIR , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_NOIR , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , EAU , EAU , TERRE , EAU , EAU , TERRE ) ,
		( TERRE , TERRE , TERRE , TERRE , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , TERRE , PIEGE_BLANC , TERRE , TERRE , TERRE ) ,
		( TERRE , TERRE , PIEGE_BLANC , TANIERE_BLANC , PIEGE_BLANC , TERRE , TERRE )
	)

# Liste des types de pion (la force d'un pion correspond à l'indice de ce pion  + 1
# 		exemple : Le loup se trouve à l'indice 3. Sa force est donc de 3 + 1 c.à.d. 4)
pions = ( 'rat' , 'chat' , 'chien' , 'loup' , 'panthère' , 'tigre' , 'lion' , 'éléphant'  )

# Position initiale des pions noirs (tuple de tuples)
posInitPionsNoirs = ( ( 3 , 1 ) , ( 2 , 6 ) , ( 2 , 2 ) , ( 3 , 5 ) , ( 3 , 3 ) , ( 1 , 7 ) , ( 1 , 1 ) , ( 3 , 7 ) )

# Position initiale des pions blancs (tuple de tuples)
posInitPionsBlancs = ( ( 7 , 7 ) , ( 8 , 2 ) , ( 8 , 6 ) , ( 7 , 3 ) , ( 7 , 5 ) , ( 9 , 1 ) , ( 9 , 7 ) , ( 7 , 1 ) )

# Position des pions noirs

posPionsNoirs = []
posPionsBlancs = []
	

# VARIABLES GLOBALES de l'Interface Graphique Utilisateur (GUI)

# Pions blancs
pionsBlancs = [ None , None , None , None , None , None , None , None ]

# Pions noirs
pionsNoirs = [ None , None , None , None , None , None , None , None ]

# Bouton radio associé aux camps (couleurs)

brNoir = None
brBlanc = None

# Variable associée au camp (couleur) qui doit jouer son tour
svCouleur = None

# Variable associée au pion sélectionné 
svPion = None

# Boutons radio associés aux types de pion

brPions = [ None , None , None , None , None , None , None , None ]

# Boutons associés aux directions

btnNord = None
btnEst = None
btnSud = None
btnOuest = None


# FONCTIONS

def selectionnerPion() :
	pion = svPion.get()
	couleur = svCouleur()
	directionsOk = getDirectionsPossibles( couleur , pion )
	activerDirectionsPossibles( directions )
	


def deplacerNord() :
	print( 'NORD :' , svCouleur.get() , svPion.get() )
	
	fin = deplacerPion( svCouleur.get() , svPion.get() , NORD )
	if fin == True :
		showinfo( 'pyXouDouQi' , 'Victoire du camp ' + str( svCouleur.get() ) + ' !!!  ' )
	else :
		passerAuTourSuivant()
	

def deplacerEst() :
	print( 'EST :' , svCouleur.get() , svPion.get() )	
	fin = deplacerPion( svCouleur.get() , svPion.get() , EST )
	if fin == True :
		showinfo( 'pyXouDouQi' , 'Victoire du camp ' + str( svCouleur.get() ) + ' !!!  ' )
	else :
		passerAuTourSuivant()
	

def deplacerSud() :
	print( 'SUD :' , svCouleur.get() , svPion.get() )	
	fin = deplacerPion( svCouleur.get() , svPion.get() , SUD )
	if fin == True :
		showinfo( 'pyXouDouQi' , 'Victoire du camp ' + str( svCouleur.get() ) + ' !!!  ' )
	else :
		passerAuTourSuivant()
	

def deplacerOuest() :
	print( 'OUEST :' , svCouleur.get() , svPion.get() )	
	fin = deplacerPion( svCouleur.get() , svPion.get() , OUEST )
	if fin == True :
		showinfo( 'pyXouDouQi' , 'Victoire du camp ' + str( svCouleur.get() ) + ' !!!  ' )
	else :
		passerAuTourSuivant()


def dessinerPion( pion , couleur ) :
	ind = pions.index( pion )
	print( 'ind : ' , ind )
	force = ind + 1
	if couleur == 'noir' :
		ligne = posInitPionsNoirs[ ind ][ 0 ]
		colonne = posInitPionsNoirs[ ind ][ 1 ]
	else :
		ligne = posInitPionsBlancs[ ind ][ 0 ]
		colonne = posInitPionsBlancs[ ind ][ 1 ]
		
	x = D * colonne - D + colonne + D // 2 + 1
	y = D * ligne - D + ligne + D // 2 + 1
	
	if couleur == 'noir' :
		pionsNoirs[ ind ] = plateau.create_text( x , y , text = str( force ) , font = ( 'TkDefaultFont' , '30' , 'bold'  ) , fill = 'black' )
	else :
		pionsBlancs[ ind ] = plateau.create_text( x , y , text = str( force ) , font = ( 'TkDefaultFont' , '30' , 'bold'  ) , fill = 'white' )


def positionnerPions() :
	for pion in pions :
		dessinerPion( pion , 'noir' )
		dessinerPion( pion , 'blanc' )
	
	
def dessinerCase( ligne , colonne , terrain = TERRE ) :
	
	x1 = D * colonne - D + colonne + 1
	x2 = ( D + 1 ) * colonne
	
	y1 = D * ligne - D + ligne + 1
	y2 = ( D + 1 ) * ligne
	
	if terrain == TERRE :
		plateau.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' )
	elif terrain == EAU :
		plateau.create_rectangle( x1 , y1 , x2 , y2 , outline = 'blue' , fill = 'blue' )
	elif terrain == PIEGE_BLANC or terrain == PIEGE_NOIR :
		plateau.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray50' )
	elif terrain == TANIERE_BLANC or terrain == TANIERE_NOIR :
		plateau.create_rectangle( x1 , y1 , x2 , y2 , outline = 'green' , fill = 'green' , stipple = 'gray75' )
	

def creerPlateau() :
	
	for ligne in range( 1 , NB_LIGNES + 1 ) :
		for colonne in range( 1 , NB_COLONNES + 1 ) :
			dessinerCase( ligne , colonne , jungle[ ligne - 1 ][ colonne - 1 ] )
			

def creerGUI() :
	
	global fenetre , plateau
	global svCouleur , svPion
	global brBlanc , brNoir
	global btnNord , btnEst , btnSud , btnOuest
	
	fenetre = Tk()
	fenetre.title( 'pyXouDouQi' )
	
	plateau = Canvas( fenetre )
	plateau[ 'width'] = 365
	plateau[ 'height'] = 469
	plateau[ 'background' ] = 'black'
	
	pwCommandes = PanedWindow( fenetre ) 
	pwCommandes[ 'orient' ] = VERTICAL
	
	lblCouleurs = Label( pwCommandes )
	lblCouleurs[ 'text' ] = 'Couleurs :'
	lblCouleurs[ 'anchor' ] = 'w'
	lblCouleurs[ 'font' ] = ( 'TkDefaultFont' , '10' , 'bold' )
	
	
	lblPions = Label( pwCommandes )
	lblPions[ 'text' ] = 'Pions :'
	lblPions[ 'anchor' ] = 'w'
	lblPions[ 'font' ] = ( 'TkDefaultFont' , '10' , 'bold' )
	
	lblDirections = Label( pwCommandes )
	lblDirections[ 'text' ] = 'Directions :'
	lblDirections[ 'anchor' ] = 'w'
	lblDirections[ 'font' ] = ( 'TkDefaultFont' , '10' , 'bold' )
	
	pwCouleurs = PanedWindow( pwCommandes , relief = GROOVE )
	
	svCouleur = StringVar()
	svCouleur.set( 'blanc' )
	
	brBlanc = Radiobutton( pwCouleurs , text = 'Blanc' , variable = svCouleur , value = 'blanc' , width = 5 )
	brNoir = Radiobutton( pwCouleurs , text = 'Noir' , variable = svCouleur , value = 'noir' , width = 5 )
	
	brNoir.pack( side = RIGHT )
	brBlanc.pack( side = RIGHT )
	
	brNoir[ 'state' ] = 'disabled'
	
	pwPions = PanedWindow( pwCommandes , relief = GROOVE )
	
	svPion = StringVar()
	svPion.set( 'chat' )
	
	brPions[ 7 ] = Radiobutton( pwPions , text = 'Éléphant (8)' , variable = svPion , value = 'éléphant' )
	brPions[ 6 ] = Radiobutton( pwPions , text = 'Lion (7)' , variable = svPion , value = 'lion' )
	brPions[ 5 ] = Radiobutton( pwPions , text = 'Tigre (6)' , variable = svPion , value = 'tigre' )
	brPions[ 4 ] = Radiobutton( pwPions , text = 'Panthère (5)' , variable = svPion , value = 'panthère' )
	brPions[ 3 ] = Radiobutton( pwPions , text = 'Loup (4)' , variable = svPion , value = 'loup' )
	brPions[ 2 ] = Radiobutton( pwPions , text = 'Chien (3)' , variable = svPion , value = 'chien' )
	brPions[ 1 ] = Radiobutton( pwPions , text = 'Chat (2)' , variable = svPion , value = 'chat' )
	brPions[ 0 ] = Radiobutton( pwPions , text = 'Rat (1)' , variable = svPion , value = 'rat' )
	
	brPions[ 7 ][ 'activeforeground' ] = 'blue'
	brPions[ 6 ][ 'activeforeground' ] = 'blue'
	brPions[ 5 ][ 'activeforeground' ] = 'blue'
	brPions[ 4 ][ 'activeforeground' ] = 'blue'
	brPions[ 3 ][ 'activeforeground' ] = 'blue'
	brPions[ 2 ][ 'activeforeground' ] = 'blue'
	brPions[ 1 ][ 'activeforeground' ] = 'blue'
	brPions[ 0 ][ 'activeforeground' ] = 'blue'
	
	brPions[ 7 ][ 'command' ] = selectionnerPion
	brPions[ 6 ][ 'command' ] = selectionnerPion
	brPions[ 5 ][ 'command' ] = selectionnerPion
	brPions[ 4 ][ 'command' ] = selectionnerPion
	brPions[ 3 ][ 'command' ] = selectionnerPion
	brPions[ 2 ][ 'command' ] = selectionnerPion
	brPions[ 1 ][ 'command' ] = selectionnerPion
	brPions[ 0 ][ 'command' ] = selectionnerPion
	
	brPions[ 7 ].grid( row = 0 , column = 0 , sticky = 'w' )
	brPions[ 6 ].grid( row = 0 , column = 1 , sticky = 'w' )
	brPions[ 5 ].grid( row = 1 , column = 0 , sticky = 'w' )
	brPions[ 4 ].grid( row = 1 , column = 1 , sticky = 'w' )
	brPions[ 3 ].grid( row = 2 , column = 0 , sticky = 'w' )
	brPions[ 2 ].grid( row = 2 , column = 1 , sticky = 'w' )
	brPions[ 1 ].grid( row = 3 , column = 0 , sticky = 'w' )
	brPions[ 0 ].grid( row = 3 , column = 1 , sticky = 'w' )

	
	pwDirections = PanedWindow( pwCommandes , relief = GROOVE ) 
	
	btnNord = Button( pwDirections , text = 'Nord' , width = 5 )
	btnEst = Button( pwDirections , text = 'Est' , width = 5 )
	btnSud = Button( pwDirections , text = 'Sud' , width = 5 )
	btnOuest = Button( pwDirections , text = 'Ouest' , width = 5 )
	
	btnNord[ 'activeforeground' ] = 'blue'
	btnEst[ 'activeforeground' ] = 'blue'
	btnSud[ 'activeforeground' ] = 'blue'
	btnOuest[ 'activeforeground' ] = 'blue'
	
	btnNord[ 'command' ] = deplacerNord
	btnEst[ 'command' ] = deplacerEst
	btnSud[ 'command' ] = deplacerSud
	btnOuest[ 'command' ] = deplacerOuest
	
	btnNord.grid( row = 0 , column = 1 , sticky = 'ew' , padx = 5 , pady = 5 )
	btnEst.grid( row = 1 , column = 2 , sticky = 'ew' , padx = 5 , pady = 5 )
	btnOuest.grid( row = 1 , column = 0 , sticky = 'ew' , padx = 5 , pady = 5 )
	btnSud.grid( row = 2 , column = 1 , sticky = 'ew' , padx = 5 , pady = 5 )
	
	plateau.pack( side = LEFT , fill = BOTH , pady = 2 , padx = 2 )
	pwCommandes.pack( side = LEFT , fill = BOTH , pady = 2 , padx = 2 )
	
	lblCouleurs.pack( side = TOP , fill = X , pady = 2 , padx = 2 )
	pwCouleurs.pack( side = TOP , fill = BOTH , pady = 2 , padx = 2 )
	
	Frame( pwCommandes , height = 20 ).pack( side = TOP , fill = BOTH , pady = 2 , padx = 2 )
	
	lblPions.pack( side = TOP , fill = X , pady = 2 , padx = 2 )
	pwPions.pack( side = TOP , fill = BOTH , pady = 2 , padx = 2 )
	
	Frame( pwCommandes , height = 20 ).pack( side = TOP , fill = BOTH , pady = 2 , padx = 2 )
	
	lblDirections.pack( side = TOP , fill = X , pady = 2 , padx = 2 )
	pwDirections.pack( side = TOP , fill = BOTH , pady = 2 , padx = 2 )


def initialiserJeu() :
	print( posInitPionsNoirs )
	for unePosition in posInitPionsNoirs :
		posPionsNoirs.append( [] )
		posPionsNoirs[ -1 ].append( unePosition[ 0 ] )
		posPionsNoirs[ -1 ].append( unePosition[ 1 ] )
	print( posPionsNoirs )
		
	print( posInitPionsBlancs )
	for unePosition in posInitPionsBlancs :
		posPionsBlancs.append( [] )
		posPionsBlancs[ -1 ].append( unePosition[ 0 ] )
		posPionsBlancs[ -1 ].append( unePosition[ 1 ] )
	print( posPionsBlancs )
	

def deplacerPion( couleur , pion , direction ) :
	
	ind = pions.index( pion )
	print( 'Pion :' , ind )
	
	if couleur == 'noir' :
		positions = posPionsNoirs
		idPion = pionsNoirs[ ind ]
	else :
		positions = posPionsBlancs
		idPion = pionsBlancs[ ind ]
		
	if direction == NORD :
		plateau.move( idPion , 0 , -1 * ( D + 1 ) )
		positions[ ind ][ 0 ] = positions[ ind ][ 0 ] - 1
		
	elif direction == EST :
		plateau.move( idPion , D + 1 , 0 )
		positions[ ind ][ 1 ] = positions[ ind ][ 1 ] + 1
		
	elif direction == SUD :
		plateau.move( idPion , 0 , D + 1 )
		positions[ ind ][ 0 ] = positions[ ind ][ 0 ] + 1
		
	elif direction == OUEST :
		plateau.move( idPion , -1 * ( D + 1 ) , 0 )
		positions[ ind ][ 1 ] = positions[ ind ][ 1 ] - 1
	
	
	ligne = positions[ ind ][ 0 ]
	colonne = positions[ ind ][ 1 ]
	
	if couleur == 'noir' and jungle[ ligne - 1 ][ colonne - 1 ] == TANIERE_BLANC :
		return True
	elif couleur == 'blanc' and jungle[ ligne - 1 ][ colonne - 1 ] == TANIERE_NOIR :
		return True
	else :
		return False
	
	
def passerAuTourSuivant() :
	if svCouleur.get() == 'noir' :
		svCouleur.set( 'blanc' )
		brNoir[ 'state' ] = 'disabled'
		brBlanc[ 'state' ] = 'active'
	else :
		svCouleur.set( 'noir' ) ;
		brNoir[ 'state' ] = 'active'
		brBlanc[ 'state' ] = 'disabled'

	
	
def getOccupant( ligne , colonne ) :
	for ind in range( len( posPionsNoirs ) ) :
		if posPionsNoirs[ ind ] != None :
			if posPionsNoirs[ ind ][ 0 ] == ligne and posPionsNoirs[ ind ][ 1 ] == colonne :
				return ( 'noir' , pions[ ind ] )
	
	for ind in range( len( posPionsBlancs ) ) :
		if posPionsBlancs[ ind ] != None :
			if posPionsBlancs[ ind ][ 0 ] == ligne and posPionsBlancs[ ind ][ 1 ] == colonne :
				return ( 'blanc' , pions[ ind ] )
	
	return None
	


def activerDirectionsPossibles( directions ) :
	if NORD in directions :
		btnNord[ 'state' ] = 'active'
	else :
		btnNord[ 'state' ] = 'disabled'
		
	if EST in directions :
		btnEst[ 'state' ] = 'active'
	else :
		btnEst[ 'state' ] = 'disabled'
		
	if SUD in directions :
		btnSud[ 'state' ] = 'active'
	else :
		btnSud[ 'state' ] = 'disabled'
		
	if OUEST in directions :
		btnOuest[ 'state' ] = 'active'
	else :
		btnOuest[ 'state' ] = 'disabled'
	


if __name__ == '__main__' :
	
	creerGUI()
	creerPlateau()
	positionnerPions()
	initialiserJeu()
	
	for ligne in range( 1 , NB_LIGNES + 1 ) :
		for colonne in range( 1 , NB_COLONNES + 1 ) :
			print( ligne , ',' , colonne , ':' , getOccupant( ligne , colonne ) )
	

	fenetre.mainloop()
