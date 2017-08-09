class ClubsController < ApplicationController

	def index 
	  @clubs = Club.all
	end

	def show
	  @club = Club.find_by club_id: params[:id]
	end
end
