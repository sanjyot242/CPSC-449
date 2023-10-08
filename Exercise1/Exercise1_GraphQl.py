import requests

url = "http://localhost:4000/graphql"


body = ["""
query getAlbumsByName {
  artists(where: {Name: "Red Hot Chili Peppers"}) {
    artistId
    name
    albums {
      title
    }
  }
}
""",
"""query getGenresByArtistName {
  artists(where: {Name: "U2"}) {
    artistId
    albums {
      albumId
      tracks {
        genreId
         genre{
          name
        }    
        
      }
      }

      }
     
    }""","""query {
  playlists(where:{Name:"Grunge"}){
    playlistId
    tracks{
      trackId
        name
        album{
	title
          artist{
            name
          }
        }
      }
    }
  }"""]



for i in range(0,3):
  response = requests.get(url=url ,json={"query":body[i]})
 # print("response status code: ", response.status_code)
  if response.status_code == 200:
      data = response.json()
       
      if i == 0:
          print("--Query 1--  #############Albums by the artist Red Hot Chili Peppers ###############")
          albums = data["data"]["artists"][0]["albums"]
          for album in albums:
            print(album["title"])
      
      elif i == 1:
          print("--Query 2-- ############# Genres associated with the artist U2 #############")
          distinct_genre_names = set()
          # Extract and store distinct genre names
          artists = data["data"]["artists"]
          for artist in artists:
              albums = artist["albums"]
              for album in albums:
                  tracks = album["tracks"]
                  for track in tracks:
                      genre_name = track["genre"]["name"]
                      distinct_genre_names.add(genre_name)

          # Print distinct genre names
          for genre_name in distinct_genre_names:
              print(genre_name)
            
      elif i == 2:
          print("--Query 3-- ############# Names of tracks on the playlist “Grunge” and their associated artists and albums #############")
          tracks = data["data"]["playlists"][0]["tracks"]
          for track in tracks:
              name = track["name"]
              title = track["album"]["title"]
              artist_name = track["album"]["artist"]["name"]
              print(f"{name}, {title}, {artist_name}")

      else:
        print("lol")
  
  else :
     print("Error is request ",response.status_code)
  
       
 
     




