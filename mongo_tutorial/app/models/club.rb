class Club
  include Mongoid::Document
  store_in collection: "club_collection"

  field :club_name, type: String
  field :season, type: Hash
  field :club_id, type: Integer
  field :primary_color, type: String
  field :secondary_color, type: String
end
