
# Deploy as a web service using Sinatra
# before you'll be able to run this you'll need 'gem install sinatra'

require 'sinatra'

require_relative 'ticket_office.rb'

post '/reserve' do
  office = TicketOffice.new()
  office.make_reservation(request.body)
end

configure do
  set :port, '8083'
end